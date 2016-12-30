from flask import Flask, render_template, redirect

import sys, getopt
import json
from lib import config

app = Flask(__name__)
nodes = {}

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/register/irnode/<name>', methods=['POST', 'PUT'])
def registerIrNode(name):
      nodes[name] = {
            
      }           

      return json.dumps({ 'status' : '1' })

@app.route('/configuration/irnode/<name>', methods=['GET'])
def irnodeConfiguration(name):
      if name not in nodes:
            return json.dumps({})

      #read our config
      devices = config.readNodeDevices()      

      if name not in devices:
            return json.dumps({})

      return json.dumps({
            'devices' : devices[name]
      })

if __name__ == "__main__":
      conf = config.readOrchestratorConfig()

      app.run(host=conf['address'], port=int(conf['port']), debug=True)