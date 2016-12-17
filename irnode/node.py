from flask import Flask

import lirc
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)    