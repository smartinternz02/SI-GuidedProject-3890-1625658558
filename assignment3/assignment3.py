import wiotp.sdk.device
import time
import random

myConfig = { 
    "identity": {
        "orgId": "1zlsjs",
        "typeId": "Assignment3",
        "deviceId":"54913"
    },
    "auth": {
        "token": "8987000566"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    #if(m == "lighton"):
        #print("....Light is ON....")
    #elif(m == "lightoff"):
        #print("....Light is OFF....")
    #print()
    

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    level=random.randint(0,100)
    intensity=random.randint(0,100)
    myData={'level':level, 'intensity':intensity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
