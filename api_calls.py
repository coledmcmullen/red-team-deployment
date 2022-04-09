#api_calls.py

import requests
import json
#import urllib
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
	session_tok = sess.json()

	if(sess.status_code == 201):
		return session_tok;
	else:
		#TODO
		printError("Failed to get session token")
		return -1

def getVMList(api_base, session_tok, vm_names):
	resp = requests.get("{}/api/vcenter/vm".format(api_base), verify=True, headers={
		"vmware-api-session-id": session_tok
	},
	params = {
		#"folders":[urllib.parse.quote_plus("Spring 2022 Laforge Senior Project")]
		"names": vm_names
		#"power_states":["POWERED_ON"]
		#"vms":["vm-18106"]
	})
	print(resp.status_code)
	return resp.json()
	#return resp.json()[0]["vm"]

#def createVM():
	#TODO

def cloneVM(api_base, session_tok, source_id, clone_name):
	resp = requests.post("{}/api/vcenter/vm?action=clone".format(api_base), verify=True, headers={
		"vmware-api-session-id": session_tok
	},
	json = {
		"name": clone_name,
		"source": source_id
	})
	#print(resp.status_code)
	return resp.json()

#204 success, 400 VM powered on, 404 not found
def deleteVM(api_base, session_tok, vm_id):
	resp = requests.delete("{}/api/vcenter/vm/{}".format(api_base, vm_id), verify=True, headers={
		"vmware-api-session-id": session_tok
	})
	return resp.json()


def getVMInfo(api_base, session_tok, vm_id):
	resp = requests.get("{}/api/vcenter/vm/{}".format(api_base, vm_id), verify=True, headers={
		"vmware-api-session-id": session_tok
	})
	return resp.json()

#204 sucess, 400 VM already in desired state, 404 VM not found
def powerOnVM(api_base, session_tok, vm_id):
	resp = requests.post("{}/api/vcenter/vm/{}/power?action=start".format(api_base, vm_id), verify=True, headers={
		"vmware-api-session-id": session_tok
	})
	return resp.status_code

#204 sucess, 400 VM already in desired state, 404 VM not found
def powerOffVM(api_base, session_tok, vm_id):
	resp = requests.post("{}/api/vcenter/vm/{}/power?action=stop".format(api_base, vm_id), verify=True, headers={
		"vmware-api-session-id": session_tok
	})
	return resp.status_code

#def startVMProcess():
	#TODO
