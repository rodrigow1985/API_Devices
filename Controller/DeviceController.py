from flask import current_app, jsonify
from Model.Device import Device
from data.Devices import devices
from config.db.Database import Database
import datetime
import json

class DeviceController:
    def __init__(self) -> None:
        pass

    def getDevices():
        devices_result = []
        db = Database()
        db.execute("SELECT * FROM devices")
        devices = db.fetchall()
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
        deviceFound = [
            device for device in devices if device['id'] == id.lower()]
        if (len(deviceFound) > 0):
            #return jsonify({'task': taskFound[0]})
            return deviceFound[0]
        return False

    def addDevice(self, device):
        response = False
        new_device = {
            'id': device.id,
            'name': device.name,
            'code': device.code,
            'description': device.description,
            'image': device.image,
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now()
        }
        # TODO: validar que el "id" no exista
        # TODO: devices son todos los devices de la BD
        devices.append(new_device)
        response = True
        return response

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