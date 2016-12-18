from flask import Flask, render_template, redirect

import sys, getopt
from lib import config

app = Flask(__name__)
nodes = {}

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/register/irnode/<name>', methods=['POST', 'PUT'])
def registerIrNode(name):
      nodes[name] = {}

if __name__ == "__main__":
      app.run(host='0.0.0.0', debug=True)