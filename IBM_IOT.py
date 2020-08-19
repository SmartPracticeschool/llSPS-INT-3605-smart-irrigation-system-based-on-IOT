import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
organization = "g5w0t4"
deviceType = "raspberry_pi"
deviceId = "123456"
authMethod = "token"
authToken = "12345678"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        print(type(cmd.data))
        i=cmd.data['command']
        if i=='motorON':
                print("Motor is on")
        elif i=='motorOFF':
                print("Motor is off")

try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        
        moist=random.randint(10,40)
        temp =random.randint(30,80)
        data = { 'Temperature' : temp, 'Moisture': moist }
        if moist<=50:
                r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=PGmSojzFqKwhN45ti0D1dpBUuAnr3xRMb7CQagce6f2XYJsZWVXU1SZuCABYlaoNE7x46sczHPgpGb0O&sender_id=FSTSMS&message=LOW%20MOISTURE&language=english&route=p&numbers=97********')
                print(r.status_code)
        
  
        
        def myOnPublishCallback():
            print ("Published Temperature Value = %s C and " % temp, "Moisture Content = %s %%" % moist, "to IBM Watson")

        success = deviceCli.publishEvent("Smart_Irrigation", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()
