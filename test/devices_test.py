import unittest
import requests
import os
import time

def time_measurement(funcion):
    def fuction_measurement(*args, **kwargs):
        start = time.time()
        c = funcion(*args, **kwargs)
        execution_time = time.time() - start
        print('Tiempo de ejecución: ' + str("{:.3f}".format(execution_time)))
        print('.............................')
        return c
    return fuction_measurement

class TestDeviceAPI(unittest.TestCase):
    host = os.getenv('API_HOST') or 'localhost'
    port = os.getenv('API_PORT') or '3003'
    api_version = os.getenv('API_VERSION') or 'v1'
    URL = "http://" + host + ":" + port + "/" + api_version + "/devices"
    example_device = {
        "name": "device_emample_name",
        "description": "device example description",
        "code": "9999",
        "image": "http://url_image_device_example"
        }
    id_prueba = 1

    def allTest(self):
        self.test_1_addDevice()
        self.test_3_getDevices()
        self.test_2_getDevice()
        self.test_4_updateDevice()
        self.test_5_deleteDevice()

    @time_measurement
    def test_1_addDevice(self):
        resp = requests.post(self.URL, json=self.example_device)
        if (resp.json()['new_id']):
            self.id_prueba = resp.json()['new_id']
        self.assertEqual(resp.status_code, 200)
        print("Test 1 'addDevice' completed. New id " + str(self.id_prueba))  

    @time_measurement
    def test_2_getDevice(self):
        print(self.id_prueba)
        resp = requests.get(self.URL + "/" + str(self.id_prueba))
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(resp.json()), 1)
        print("Test 2 'getDevice' completed with id " + str(self.id_prueba))

    @time_measurement
    def test_3_getDevices(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(resp.json()), 1)
        print("Test 3 'getDevices' completed")
    
    @time_measurement
    def test_4_updateDevice(self):
        resp = requests.put(self.URL + "/" + str(self.id_prueba), json=self.example_device)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 1)
        print("Test 4 'updateDevice' completed with id " + str(self.id_prueba))

    @time_measurement
    def test_5_deleteDevice(self):
        resp = requests.delete(self.URL + "/" + str(self.id_prueba))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 1)
        print("Test 5 'deleteDevice' completed with id " + str(self.id_prueba))