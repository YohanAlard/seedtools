#!/usr/bin/python
import redis
import os
import json
import subprocess
import collections 
r = redis.StrictRedis(host='localhost', port=6379, db=0)
uptimes= []
temperatures = []
if r.get('uptimes'):
	uptimes = json.loads(r.get('uptimes'))
if r.get('temperatures'): 
	temperatures = json.loads(r.get('temperatures'))

updateShell = subprocess.Popen('uptime', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
outUpdateTime, err = updateShell.communicate()
print outUpdateTime
temperatureShell = subprocess.Popen(['vcgencmd','measure_temp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
outTemperature, err = temperatureShell.communicate()
print outTemperature

	
temperatures.insert(0, outTemperature)
uptimes.insert(0,outUpdateTime)
#newTemp = collections.deque(temperatures, 50)
#r.set('temperatures', json.dumps(newTemp))
r.set('temperatures', json.dumps(temperatures))
r.set('uptimes', json.dumps(uptimes))

