import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "1zlsjs",
        "typeId": "VITshre",
        "deviceId":"700425"
    },
    "auth": {
        "token": "7004251110"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()

