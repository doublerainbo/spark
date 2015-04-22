'''
Created on Apr 4, 2015

@author: doublerainbo
'''
from APIClient import login

client = login()

result = client.send_get("v1/devices/")

device = result[0]
deviceId = device["id"]

print client.send_post("v1/devices/" + deviceId + "/led", {"params": "l8,LOW"})