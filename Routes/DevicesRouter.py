from Controller.DeviceController import DeviceController
from flask import Flask, jsonify, request, Blueprint
import os

#from __main__ import app

DEVICE_API = Blueprint('device_api', __name__)

def get_blueprint():
    """Return the blueprint for the main DEVICE_API module"""
    return DEVICE_API

devices = DeviceController()

api_version = '/' + os.getenv('API_VERSION') or 'v1'

# Every devices
@DEVICE_API.route(api_version + '/devices', methods=['GET'])
def getDevices():
    return DeviceController.getDevices()

# Single Device
@DEVICE_API.route(api_version + '/devices/<string:device_id>', methods=['GET'])
def getDevice(device_id):
    deviceFound = devices.getDevice(device_id)
    if (deviceFound != False):
        return deviceFound
    return jsonify({'message': 'Device Not found'}), 400

# Create device
@DEVICE_API.route(api_version + '/devices', methods=['POST'])
def addDevice():
    id = devices.addDevice(request.json)
    if (id > 0):
        return jsonify({'new_id': id})
    return jsonify({'message': 'Device can not be added'})
    
#Update device
@DEVICE_API.route(api_version + '/devices/<string:device_id>', methods=['PUT'])
def editDevice(device_id):
    new_updated_at = devices.updateDevice(device_id, request.json)
    if (new_updated_at != False):
        return jsonify({'new_updated_at': new_updated_at})
    return jsonify({'message': 'Device can not be updated'})

#Delete device
@DEVICE_API.route(api_version + '/devices/<string:device_id>', methods=['DELETE'])
def deleteDevice(device_id):
    new_deleted_at = devices.deleteDevice(device_id)
    if (new_deleted_at != False):
        return jsonify({'device_deleted_at': new_deleted_at})
    return jsonify({'message': 'Device can not be deleted'})