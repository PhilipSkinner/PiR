from flask import Flask, render_template

import lirc

app = Flask(__name__)

@app.route('/')
def index():
  lirc.sendCommand('test', 'test')

  return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
