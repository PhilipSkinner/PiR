from flask import Flask

import lirc
import json

from lib import config

app = Flask(__name__)
devices = {}

#get a list of all devices
@app.route('/devices', methods=['GET'])
def getDevices():
    return ''

@app.route('/devices', methods=['POST'])
def createDevice():
    return ''

@app.route('/devices/<id>', methods=['GET'])
def getDevice(id):
    return ''

@app.route('/devices/<id>', methods=['PUT'])
def saveDevice(id):
    return ''

@app.route('/device/<id>', methods=['DELETE'])
def deleteDevice(id):
    return ''

@app.route('/devices/<id>/commands', methods=['GET'])
def getDeviceCommands(id):
    return ''

@app.route('/devices/<id>/commands/<command>', methods=['GET'])
def runDeviceCommand(id, command):
    return ''