import webiopi
import os

from webiopi.devices.serial import Serial

serialUSB = Serial("ttyUSB0", 9600)
sensors = [0 for a in range(6)]

#def setup():
#    while (serialUSB.available() > 0):
#        serialUSB.readString()	

def loop():
	
	if (serialUSB.available() > 0):
		try:
			data = serialUSB.readString()
		except:
			pass
		lines = data.split("\r\n")
		count = len(lines)
		lines = lines[0:count-1]

		for pair in lines:
			cv = pair.split("=")
			try:
				channel = int(cv[0])
			except :
				pass
				
				
			try:
				value = cv[1]
			except  :
				pass
			try:
				sensors[channel] = value
			except  :
				pass
		
	webiopi.sleep(1)
	

	

@webiopi.macro
def getSensor(channel):
	out = (sensors[int(channel)] )
	return  out


@webiopi.macro
def osTemp():
	res = os.popen('vcgencmd measure_temp').readline()
	rres=res.replace("temp=","").replace("'C\n","")
	return rres
	
@webiopi.macro
def osIp():
	ip = os.popen('hostname -I').readline()
	
	return ip

@webiopi.macro	
def osUP():
	up = os.popen('uptime -p').readline()
	uup=up.replace("up ","").replace("'C\n","")
	return uup
	
#added 1/3/18 	
@webiopi.macro
def serial(value):
	serialUSB.writeString(value)