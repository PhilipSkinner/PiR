from flask import Flask, render_template, redirect

import lirc
import hive.api
import sys, getopt

username = None
password = None
api = None
app = Flask(__name__)

@app.route('/')
def index():  
  return render_template('index.html', lights=api.lights)

@app.route('/light/off/<id>')
def lightOff(id=None):
  api.lightOff(id)
  return redirect('/')

@app.route('/light/on/<id>')
def lightOn(id=None):
  api.lightOn(id)
  return redirect('/')

@app.route('/light/brightness/<id>/<level>')
def lightBrightness(id=None, level=None):
  api.setBrightness(id, level)
  return redirect('/')

if __name__ == "__main__":
  opts, args = getopt.getopt(sys.argv[1:],'u:p:', ['username=', 'password='])  

  for opt, arg in opts:      
    if opt in ('-u', '--username'):
      username = arg
    if opt in ('-p', '--password'):
      password = arg

  #login to hive
  api = hive.api.API(username, password)

  app.run(host='0.0.0.0', debug=True)
