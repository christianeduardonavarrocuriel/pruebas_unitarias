import requests
import json
import random
import time

url ="https://iotdemo-ff8be-default-rtdb.firebaseio.com/sensores/sucursal1.json"

def get_sensores():
    response = requests.get(url)
    print(response.status_code)
    print(response.text)

def simular_sensores():
    while True:
        data = {
            "temperatura": random.randint(15, 30),
            "humedad": random.randint(30, 70)
        }
        response = requests.put(url, data=json.dumps(data))
        print(response.status_code)
        print(response.text)
        time.sleep(5)

if __name__ == "__main__":
    #get_sensores()
    simular_sensores()