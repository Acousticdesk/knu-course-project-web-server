from flask import Flask, request
import numpy as np
from flask_cors import CORS
from model.model import lm_HPRICE7
import math

app = Flask(__name__)
CORS(app)

@app.route('/prediction', methods=['POST'])
def get_prediction():
    body = request.json

    real_estate = {
        'logarea': np.log(body['area']),
        'rooms': body['rooms'],
        'ceilingHeight': body['ceilingHeight'],
        'numApartmentsTotal': body['numApartmentsTotal'],
        'floor': body['floor'],
        'crimeRateInDistrict': body['crimeRateInDistrict'],
        'predictedClass': body['predictedClass']
    }

    print(real_estate)

    logprice_predicted = lm_HPRICE7.predict(real_estate).values[0]

    predicted_price = math.exp(logprice_predicted)
    print(predicted_price)
    price_formatted = "{:,}".format(round(predicted_price))

    return {'prediction': str(price_formatted)}

if __name__ == '__main__':
    app.run()
