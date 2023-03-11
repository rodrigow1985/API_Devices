from crypt import methods
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

import Routes.DevicesRouter

@app.route('/')
def home():
    return jsonify({"Message":"Welcome to HomeServer API"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003, debug=True)