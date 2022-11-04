from tkinter import *


import sensors

import random

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "project/#"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


class PyProject(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()

    def consultar(self):
        ciudad = self.display.get()
        sensors.sensors_init(ciudad);

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def createWidgets(self):
        self.display = Entry(self, font=("Arial", 24), relief=RAISED, justify=CENTER, bg='white', fg='black',
                             borderwidth=0)
        self.display.insert(0, "Inserte una ciudad")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.startButton = Button(self, font=("Arial",12), fg='black', text='Consultar',highlightbackground='white', command=lambda: self.consultar())
        self.startButton.grid(row=1, column=0, columnspan=4,  sticky="nsew")

        self.temperaturaLabel = Label(self, font=("Arial", 12), text="Temperatura", justify=LEFT)
        self.temperaturaLabel.grid(row=2, column=0, sticky="nsew")

        self.humedadLabel = Label(self, font=("Arial", 12), text="Humedad", justify=LEFT)
        self.humedadLabel.grid(row=3, column=0, sticky="nsew")

        self.presionLabel = Label(self, font=("Arial", 12), text="Presión", justify=LEFT)
        self.presionLabel.grid(row=4, column=0, sticky="nsew")

        self.temperatura = Label(self, font=("Arial", 12), text="Temperatura", justify=LEFT)
        self.temperatura.grid(row=2, column=1, sticky="nsew")

        self.humedad = Label(self, font=("Arial", 12), text="Humedad", justify=LEFT)
        self.humedad.grid(row=3, column=1, sticky="nsew")

        self.presion= Label(self, font=("Arial", 12), text="Presión", justify=LEFT)
        self.presion.grid(row=4, column=1, sticky="nsew")


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
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

client = connect_mqtt()
subscribe(client)
screen = Tk()
screen.title("TallerDistribuidos")
screen.resizable(True, True)
root = PyProject(screen).grid()
screen.config(cursor="circle")
screen.mainloop()
client.loop_forever()