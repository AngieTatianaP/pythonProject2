import random
import time
import requests

from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "project/humidity"
client_id = f'humidity-{random.randint(0, 1000)}' # generate client ID with pub prefix randomly


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, city):
    msg_count = 0

    time.sleep(1)
    msg = get_humidity(city)
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    msg_count += 1

def get_humidity(city):
    ciudad = city
    parametros = {"q":ciudad,
                  "units":"metric",
                  "APPID": "61ef597e17f8b84242fc06308dab1364"}

    respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)
    if respuesta.status_code == 200:
        # La respuesta json se convierte en un diccionario
        datos = respuesta.json()
        # Se obtienen los valores del diccionario
        hum = datos["main"]["humidity"]
        return hum
    else:
        return "N/A"

def run(city):
    client = connect_mqtt()
    # client.loop_start()
    publish(client, city)
