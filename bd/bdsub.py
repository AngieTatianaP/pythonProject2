# python3.6

import random
import pymongo as db
import certifi
from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "project/#"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'
bdclient = db.MongoClient("mongodb+srv://admin:admin@distribuidos.vodtfqj.mongodb.net/?retryWrites=true&w=majority",
                              tlsCAFile=certifi.where())
mydb = bdclient['project']
mycol = mydb["sensors"]

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        x = False
        if msg.topic == "project/temperature":
            temp = msg.payload.decode()
            x = mycol.insert_one({"temperatura":temp})
        if msg.topic == "project/humidity":
            hum = msg.payload.decode()
            x = mycol.insert_one({"humedad": hum})
        if msg.topic == "project/pression":
            pres = msg.payload.decode()
            x = mycol.insert_one({"presion": pres})
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if x:
            print(f"Stored in database correctly status:{x}")
        else:
            print("error")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()