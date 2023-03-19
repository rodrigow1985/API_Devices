from devices_test import TestDeviceAPI

def allTest():
    testerDeviceAPI = TestDeviceAPI()
    printHeaderTest(testerDeviceAPI.__class__.__name__)
    testerDeviceAPI.allTest()

    

def printHeaderTest(class_name):
    print('-----------------------------')
    print(class_name)
    print('-----------------------------')

if __name__ == '__main__':
    allTest()