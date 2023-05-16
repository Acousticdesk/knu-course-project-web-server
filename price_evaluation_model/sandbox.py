from model import lm_HPRICE10
import math

sample = {
    'logarea': 4.189655,
    'rooms': 2,
    'ceilingHeight': 3,
    'numApartmentsTotal': 328,
    'floor': 11,
    'crimeRateInDistrict': 2317,
    'predictedClass': 2
}

logprice_predicted = lm_HPRICE10.predict(sample).values[0]

predicted_price = math.exp(logprice_predicted)
price_formatted = "{:,}".format(round(predicted_price))

print(price_formatted)
