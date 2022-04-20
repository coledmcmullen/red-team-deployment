#backend.py

from api_calls import *

#API configuration file relative path
conf_path = "./api_conf.json"
#Hosts File relative path
hosts_path = "./hosts.json"
#Guest login file relative path
guest_path = "./guest_login.json"

#Remove
proc_spec = {
	"path": "/usr/lib/firefox-esr/firefox-esr"
}

def printError(err):
	print("Error: %s" % err)

def loadFile(fpath):
	#conf =
	try:
		f = open(fpath)
		conf = json.load(f)
		f.close()
	except Exception as e:
		#TODO
		printError(e)
		return -1
	return conf

def writeFile(fpath, data):
	try:
		f = open(fpath, "w")
		f.write(data)
		f.close()
	except Exception as e:
		#TODO handle
		printError(e)
		return -1
	return 0

def init():
	conf = loadFile(conf_path)
	hosts = loadFile(hosts_path)
	#if(conf["session_token"] == "" or conf["session_token"] == -1):
	conf["session_token"] = getSessionToken(conf["api_base"], conf["creds"])
	#writeConf(conf_path, json.dumps(conf, indent = 4))
	return conf, hosts

def testCalls():
	conf = init()
	#test_resp = getVMIDs(conf["api_base"], conf["session_token"], ["test_target"])
	#test_id = test_resp[0]["vm"]
	#test_resp = listVMFolder(conf["api_base"], conf["session_token"], ["Spring_2022_Laforge_Senior_Project"])
	#print(getVMInfo(conf["api_base"], conf["session_token"], test_id))
	#print(getVMInfo(conf["api_base"], conf["session_token"], ["rtdt_live"]))
	#print(powerOffVM(conf["api_base"], conf["session_token"], test_id))
	#print(powerOnVM(conf["api_base"], conf["session_token"], test_id))
	#print(cloneVM(conf["api_base"], conf["session_token"], test_id, "test_target"))
	#print(deleteVM(conf["api_base"], conf["session_token"], test_id))
	#test_resp = startVMProcess(conf["api_base"], conf["session_token"], test_id, guest_login, proc_spec)

def addHost(conf, hosts, source_name, clone_name):
	source_id = -1
	clone_id = -1

	#TODO - Check clone name not already used in vCenter

	#Retrieve source id by source name
	for h in hosts:
		if(h["name"] == source_name):
			source_id = h["id"]
		elif(h["name"] == clone_name):
			clone_id = h["id"]

	if(source_id == -1):
		resp = getVMIDs(conf["api_base"], conf["session_token"], source_id)
		if(resp.status_code == 200):
			source_id = resp[0]["vm"]

	#TODO handle non-success response codes

	if(source_id != -1):
		hosts.append({"id": "", "name": clone_name, "type": source_id, "powered_on": False, "is_template": False})

	writeFile(hosts_path, json.dumps(hosts, indent = 4))
	#Debug only?
	print("Added host {} of type {}/{} to model; ready to generate...".format(clone_name, source_name, source_id))
	return hosts

def removeHost(conf, hosts, host_name):
	host_id = -1

	#Retrieve source id from hosts model
	for h in hosts:
		if(h["name"] == host_name):
			host_id = h["id"]
			if(h["is_template"] == True):
				printError("Cannot remove template")
				return hosts

	#If not, get from API
	if(host_id == -1):
		try:
			resp = getVMIDs(conf["api_base"], conf["session_token"], host_name)
			host_id = resp[0]["vm"]

		except Exception as err:
			printError(err)
			printError("VM ID was not found")

	#Check vm is not template if retrieved
	resp1 = powerOffVM(conf["api_base"], conf["session_token"], host_id)
	#Check power off was successful
	resp2 = deleteVM(conf["api_base"], conf["session_token"], host_id)

	if(resp2.status_code == 204):
		for h in hosts:
			if(h["id"] == host_id):
				hosts.remove(h)
		print("Successfully deleted %s" % host_name)
	else:
		print("Failed to remove host %s" % host_name)
		#TODO handle err?

	writeFile(hosts_path, json.dumps(hosts, indent = 4))
	return hosts

def generateModel(conf, hosts):
	for h in hosts:
		#TODO move host removal here

		#deploy host if not yet deployed
		if(getVMIDs(conf["api_base"], conf["session_token"], h["name"]) == []):
			try:
				resp = cloneVM(conf["api_base"], conf["session_token"], h["type"], h["name"])
			except Exception as err:
				#Debug only?
				printError("Host {} failed to deploy from source {}".format(h["name"], h["type"]))
				#TODO - handle clone failure
				printError(err)
				return hosts

			if(resp.status_code == 200):
				h["id"] = resp.json()
				h["powered_on"] = True
				print("Deployed host {} with id {}".format(h["name"], h["id"]))

				writeFile(hosts_path, json.dumps(hosts, indent = 4))
			#else:
				#Move err message?
	return hosts

def loadModel(conf, hosts):
	for h in hosts:
		id = getVMIDs(conf["api_base"], conf["session_token"], h["name"])
		h["id"] = id[0]["vm"]
		#TODO add attribute if not found
		if(id["power_state"] == "POWERED_ON"):
			h["powered_on"] = True
		elif(id["power_state"] == "POWERED_OFF"):
			h["powered_on"] = False

		#TODO determine type - possibly pull descriptions of VM
		#TODO determine if template

	print("Hosts loaded:\n", hosts)

	writeFile(hosts_path, json.dumps(hosts, indent = 4))
	return hosts
