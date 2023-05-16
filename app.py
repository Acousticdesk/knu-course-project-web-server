from flask import Flask, request
import numpy as np
from flask_cors import CORS
from price_evaluation_model.model import lm_HPRICE10
from class_evaluation_model.model import class_evaluation_model
from translator.translator import translate_text
import math
from directions.directions import get_directions_to_city_center_in_minutes

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

trans_memo = {}
directions_memo = {}

@app.route('/class-prediction', methods=['POST'])
def get_class_prediction():
    body = request.json
    description_translated = trans_memo.get(body['description'], False)

    # print(description_translated)

    if not description_translated:
        description_translated = translate_text('en-US', body['description'])
        trans_memo[body['description']] = description_translated

    predicted_categorical = class_evaluation_model.predict([description_translated])
    predicted_class = np.argmax(predicted_categorical)

    # predicted class between Linear Regression and NN model vary, for this reason, use mapping:
    predicted_class_map = {
        0: 3,
        1: 2,
        2: 1
    }

    return {'class': str(predicted_class_map.get(predicted_class, 1))}

@app.route('/price-prediction', methods=['POST'])
def get_price_prediction():
    body = request.json

    crime_per_district = {
        'Шевченківський': 4634,
        'Дніпровський': 3939,
        "Солом'янський": 3860,
        'Оболонський': 3524,
        'Деснянський': 3022,
        'Дарницький': 2999,
        'Святошинський': 2884,
        'Печерський': 2537,
        'Голосіївський': 2317,
        'Подільський': 2106,
    }

    minutes_to_city_center = directions_memo.get(body['address'], False)

    if not minutes_to_city_center:
        print('address was not found in memo, calculating...')
        minutes_to_city_center = get_directions_to_city_center_in_minutes(body['address'])
        directions_memo[body['address']] = minutes_to_city_center

    print(minutes_to_city_center, 'walking distance to city center in minutes')

    real_estate = {
        'logarea': np.log(body['area']),
        'rooms': body['rooms'],
        # 'ceilingHeight': body['ceilingHeight'],
        # 'numApartmentsTotal': body['numApartmentsTotal'],
        # 'floor': body['floor'],
        'crimeRateInDistrict': crime_per_district.get(body['district'], 3000),
        'predictedClass': body['predictedClass'],
        'minutesToCityCenter': minutes_to_city_center
    }

    logprice_predicted = lm_HPRICE10.predict(real_estate).values[0]

    predicted_price = math.exp(logprice_predicted)
    price_formatted = "{:,}".format(round(predicted_price))

    return {'prediction': str(price_formatted)}

if __name__ == '__main__':
    app.run()
