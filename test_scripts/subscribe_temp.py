#!/usr/bin/python

ip = "127.0.0.1"
port = 3883

import paho.mqtt.client as paho
mqttc = paho.Client()
topic = "mbed/request/subscriptions/mbed-endpoint/cc69e7c5-c24f-43cf-8365-8d23bb01c707/303/0/5700"
message = "{\"path\":\"/303/0/5700\",\"ep\":\"cc69e7c5-c24f-43cf-8365-8d23bb01c707\",\"ept\":\"mbed-endpoint\",\"verb\":\"subscribe\"}"
mqttc.connect(ip, port, 60)
mqttc.publish(topic,message)
mqttc.disconnect();
