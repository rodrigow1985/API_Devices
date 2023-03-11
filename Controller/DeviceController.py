from flask import current_app, jsonify
from Model.Device import Device
from data.Devices import devices
from config.db.Database import Database
from datetime import datetime
import json

class DeviceController:
    def __init__(self) -> None:
        pass

    def getDevices():
        devices_result = []
        db = Database()
        devices = db.stored_procedure('select_devices')
        for device in devices:
            current_device = Device(device[0], device[1], device[2], device[3], device[4], device[5], device[6])
            devices_result.append(json.dumps(current_device.__dict__, default=str))
        response = current_app.response_class(
            response=devices_result,
            status=200,
            mimetype='application/json'
        )
        return response

    def getDevice(self, id):
        devices_result = []
        db = Database()
        devices = db.stored_procedure('select_divice_by_id', [id, ])
        for device in devices:
            current_device = Device(device[0], device[1], device[2], device[3], device[4], device[5], device[6])
            devices_result.append(json.dumps(current_device.__dict__, default=str))
        response = current_app.response_class(
            response=devices_result,
            status=200,
            mimetype='application/json'
        )
        return response

    def addDevice(self, name, description, code, image, created_at, updated_at):
        now = datetime.now()
        created_at = now.strftime('%Y-%m-%d %H:%M:%S')
        updated_at = now.strftime('%Y-%m-%d %H:%M:%S')
        new_device = Device(id, name, description, code, image, created_at, updated_at)
        new_id = 0
        db = Database()
        args = (new_device.name, new_device.description, new_device.code, new_device.image, new_device.created_at, 
                new_device.updated_at, new_id)
        result_args = db.callproc('add_device', args)
        return result_args[6]

    def updateDevice(self, device, device_editted):
        response = False
        device['id'] = device_editted.id
        device['name'] = device_editted.name
        device['description'] = device_editted.description
        device['image'] = device_editted.image
        device['code'] = device_editted.code
        device['updated_at'] = datetime.datetime.now()
        response = True
        return response
    
    def deleteDevice(self, device):
        response = False
        devices.remove(device)
        response = True
        return response