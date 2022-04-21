#api_calls.py

import requests
import json

def printError(err):
        print("Error: %s" % err)

def getSessionToken(api_base, api_creds):
	try:
		sess = requests.post("{}/api/session".format(api_base), auth = (api_creds["user"], api_creds["password"]), verify = True)
	except Exception as err:
		printError(err)
		return -1

	#TODO handle session creation failure
	#if(sess.status_code == 201):
	#	print("Retrieved new session token")
	#else:
	#	printError("Failed to get session token")
	#	return -1

	return sess.json()


def getVMIDs(api_base, session_tok, vm_names):
	resp = requests.get("{}/api/vcenter/vm".format(api_base), verify = True, headers = {
		"vmware-api-session-id": session_tok
	},
	params = {
		"names": vm_names
	})

	#Remove - Check status code and throw err if not successful
	#print(resp.status_code)
	#return just ID or entire json to caller? Restrict to singular ID or allow multiple ID retrieval?
	return resp.json()

def listVMFolder(api_base, session_tok, vm_folders):
	resp = requests.get("{}/api/vcenter/vm".format(api_base), verify = True, headers = {
		"vmware-api-session-id": session_tok
	},
	params = {
		#"folders": [urllib.parse.quote_plus("Spring 2022 Laforge Senior Project")]
		"folders": vm_folders
		#"power_states": ["POWERED_ON"]
		#"vms": ["vm-18106"]
	})
	return resp


#def createVM():

#200 success, 400 clone name already exists, 500 resources unavailable
def cloneVM(api_base, session_tok, source_id, clone_name):
	resp = requests.post("{}/api/vcenter/vm?action=clone".format(api_base), verify = True, headers = {
		"vmware-api-session-id": session_tok
	},
	json = {
		"name": clone_name,
		"source": source_id,
		"power_on": True
	})
	return resp


#204 success, 400 VM powered on, 404 not found
def deleteVM(api_base, session_tok, vm_id):
	resp = requests.delete("{}/api/vcenter/vm/{}".format(api_base, vm_id), verify = True, headers = {
		"vmware-api-session-id": session_tok
	})
	#return resp.json()
	return resp


def getVMInfo(api_base, session_tok, vm_id):
	resp = requests.get("{}/api/vcenter/vm/{}".format(api_base, vm_id), verify = True, headers = {
		"vmware-api-session-id": session_tok
	})
	return resp


#204 sucess, 400 VM already in desired state, 404 VM not found
def powerOnVM(api_base, session_tok, vm_id):
	resp = requests.post("{}/api/vcenter/vm/{}/power?action=start".format(api_base, vm_id), verify = True, headers = {
		"vmware-api-session-id": session_tok
	})
	return resp


#204 sucess, 400 VM already in desired state, 404 VM not found
def powerOffVM(api_base, session_tok, vm_id):
	resp = requests.post("{}/api/vcenter/vm/{}/power?action=stop".format(api_base, vm_id), verify = True, headers = {
		"vmware-api-session-id": session_tok
	})
	return resp


def startVMProcess(api_base, session_tok, vm_id, guest_login, proc_spec):
	resp = requests.post("{}/api/vcenter/vm/{}/guest/processes?action=create".format(api_base, vm_id), verify = True, headers = {
		"vmware-api-session-id": session_tok
	},
	json = {
		"credentials": guest_login,
		"spec": proc_spec
	})
	return resp


def killVMProcess(api_base, session_tok, vm_id, guest_login, pid):
	resp = requests.post("{}/api/vcenter/vm/{}/guest/processes/{}?action=delete".format(api_base, vm_id, pid), verify = True, headers = {
		"vmware-api-session-id": session_tok
	},
	json = {
		"credentials": guest_login
	})
	return resp
