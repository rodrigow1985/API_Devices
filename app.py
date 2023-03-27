from crypt import methods
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
#from Routes.DevicesRouter import DevicesRouter
import datetime
import os
import argparse

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

import Routes.DevicesRouter

# TODO
# 1) Actualizar swagger.json

# flask swagger configs
api_version = '/' + os.getenv('API_VERSION') or 'v1'
api_start_time = datetime.datetime.now()

### swagger specific ###
SWAGGER_URL = api_version + '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Home Server List API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

## Blueprints
app.register_blueprint(Routes.DevicesRouter.get_blueprint())

## Errors handlers
@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)

@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)

@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)

## Main route
@app.route('/')
def home():
    return jsonify({
        "Status":"OK",
        "API version": api_version,
        "API start at": api_start_time
                    })

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=os.getenv('API_PORT') or 3003, debug=True)
    PARSER = argparse.ArgumentParser(
        description="Seans-Python-Flask-REST-Boilerplate")

    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('API_PORT', 3003))
    if ARGS.debug:
        print("Running in debug mode")
        CORS = CORS(app)
        app.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        app.run(host='0.0.0.0', port=PORT, debug=False)