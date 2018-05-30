import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
 return 'Hello World!'

@app.route('/roll')
def roll_dice():
  a = random.randint(1,6)
  b = random.randint(1,6)
  return jsonify([a,b])

if __name__ == '__main__':
 app.debug = True
 app.run()
