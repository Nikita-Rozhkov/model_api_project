import pandas as pd
from sklearn.metrics import r2_score
from urllib import request, parse
import urllib.request
import json


def get_prediction(Power, Mileage, Gearbox, FuelType):
    body = {'Power': Power,
                            'Mileage': Mileage,
                            'Gearbox': Gearbox,
                            'FuelType': FuelType}

    myurl = "http://localhost:5000/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    #print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']

if __name__=='__main__':
    Power = 500
    Mileage = 3000
    Gearbox = 'auto'
    FuelType = 'petrol'
    preds = get_prediction(Power, Mileage, Gearbox, FuelType)
    print(preds)