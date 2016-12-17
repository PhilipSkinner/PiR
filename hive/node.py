from flask import flask

import api

api = None
app = Flask(__name__)

@app.route('/lights', methods=['GET'])
def getLights():
    return ''

@app.route('/lights/<id>', methods=['GET'])
def getLight(id):
    return ''

@app.route('/lights/<id>/state/on', methods=['PUT'])
def lightOn(id):
    api.lightOn(id)
    return ''

@app.route('/lights/<id>/state/off', methods=['PUT'])
def lightOff(id):
    api.lightOff(id)
    return ''

@app.route('/lights/<id>/brightness/<level>', methods=['PUT'])
def lightBrightness(id, level):
    api.setBrightness(id, level)
    return ''

@app.route('/switches', methods=['GET'])
def getSwitches():
    return ''

@app.route('/switches/<id>', methods=['GET'])
def getSwitch(id):
    return ''

@app.route('/switches/<id>/state/on', methods=['PUT'])
def switchOn(id):
    return ''

@app.route('/switches/<id>/state/off', methods=['PUT'])
def switchOff(id):
    return ''

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:],'u:p:', ['username=', 'password='])  

    for opt, arg in opts:      
        if opt in ('-u', '--username'):
            username = arg
        if opt in ('-p', '--password'):
            password = arg

    api = api.API(username, password)

    app.run(host='0.0.0.0', debug=True)