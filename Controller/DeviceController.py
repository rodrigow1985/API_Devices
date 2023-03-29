from flask import current_app
from Model.Device import Device
from database.Database import Database
from utils.Dict import CreateDict
import json

class DeviceController:
    def __init__(self) -> None:
        pass

    def getDevices():
        db = Database()
        devices = db.stored_procedure('select_devices')
        mydict = CreateDict()
        for index, device in enumerate(devices):
            mydict.add(index,({
                "id": device[0],
                "name": device[1],
                "description": device[2],
                "code": device[3],
                "image": device[4],
                "created_at": device[5],
                "updated_at": device[6]
                }))
        response = current_app.response_class(
            response=json.dumps(mydict, indent=2, sort_keys=True, default=str),
            status=200,
            mimetype='application/json'
        )
        return response

    def getDevice(self, id):
        db = Database()
        db_result = db.stored_procedure('select_divice_by_id', [id, ])
        device = Device(db_result[0][0], db_result[0][1], db_result[0][2], db_result[0][3], db_result[0][4], db_result[0][5], db_result[0][6])
        response = current_app.response_class(
            response=json.dumps(device.__dict__, default=str),
            status=200,
            mimetype='application/json'
        )
        return response

    def addDevice(self, request_json):
        new_device = Device("", request_json['name'], request_json['description'], request_json['code'], request_json['image'], "", "")
        new_id = 0
        db = Database()
        args = (new_device.name, new_device.description, new_device.code, new_device.image, new_id)
        result_args = db.callproc('add_device', args)
        return result_args[4]

    def updateDevice(self, id, request_json):
        new_updated_at = ""
        device_updated = Device(id, request_json['name'], request_json['description'], request_json['code'], request_json['image'], "", "")
        args = (device_updated.id, device_updated.name, device_updated.description, device_updated.code, device_updated.image, new_updated_at)
        db = Database()
        result_args = db.callproc('update_device', args)
        return result_args[5]
    
    def deleteDevice(self, id):
        new_deleted_at = ""
        args = (id, new_deleted_at)
        db = Database()
        result_args = db.callproc('delete_device', args)
        return result_args[1]