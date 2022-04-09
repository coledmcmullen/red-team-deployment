#api_calls.py

import requests
import json
#import logging

#logging.captureWarnings(True)

def loadConf(conf_filepath):
	#conf =
	try:
		f = open(conf_filepath)
		conf = json.load(f)
		f.close()
	except Exception as e:
		#TODO
		printError(e)
		return -1
	return conf

def printError(err):
	print("Error: %s" % err)

def getSessionToken(api_base, api_creds):
	sess = requests.post("{}/api/session".format(api_base), auth=(api_creds["user"], api_creds["password"]), verify=True)
	session_id = sess.json()

	if(sess.status_code == 201):
		return session_id;
	else:
		#TODO
		printError("Failed to get session token")
		return -1

def getVMList(api_base, session_id):
	resp = requests.get("{}/api/vcenter/vm".format(api_base), verify=True, headers={
	    "vmware-api-session-id": session_id
	})

	return resp.json()

#def createVM():
	#TODO

#def cloneVM():
	#TODO

#def deleteVM():
	#TODO

#def getVMInfo():
	#TODO

#def startVMProcess():
	#TODO
