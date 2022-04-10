#backend.py

from api_calls import *

#API configuration file relative path
conf_path = "./api_conf"

#TODO isolate into file
#guest_conf_path = ""
guest_login = {
	"interactive_session": True,
	"password": "<GUEST_PASS>",
	"type": "USERNAME_PASSWORD",
	"user_name": "<GUEST_USER>"
}
#TODO support optional spec args
proc_spec = {
	"path": "/usr/lib/firefox-esr/firefox-esr"
}

def loadConf(fpath):
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

def writeConf(fpath, data):
	try:
		f = open(fpath, "w")
		f.write(data)
		f.close()
	except Exception as e:
		#TODO
		printError(e)
		return -1
	return 0

def init():
	conf = loadConf(conf_path)
	#if(conf["session_token"] == "" or conf["session_token"] == -1):
	#conf["session_token"] = getSessionToken(conf["api_base"], conf["creds"])
	#writeConf(conf_path, json.dumps(conf, indent = 4))
	return conf

def testHostsModel():
	#hosts = []
	hosts = [loadConf("target2.json")]
	print(hosts[0], hosts)
	hosts[0]["id"] = 2
	print(hosts[0], hosts)
	hosts[0]["name"] = "target"
	writeConf("target.json", json.dumps(hosts[0], indent = 4))

def testCalls():
	conf = init()
	#test_resp = getVMIDs(conf["api_base"], conf["session_token"], ["test_target"])
	test_id = test_resp[0]["vm"]
	#test_resp = listVMFolder(conf["api_base"], conf["session_token"], ["Spring_2022_Laforge_Senior_Project"])
	#print(test_resp)
	#print(test_id)
	#print(getVMInfo(conf["api_base"], conf["session_token"], test_id))
	#print(getVMInfo(conf["api_base"], conf["session_token"], ["rtdt_live"]))
	#print(powerOffVM(conf["api_base"], conf["session_token"], test_id))
	#print(powerOnVM(conf["api_base"], conf["session_token"], test_id))
	#print(cloneVM(conf["api_base"], conf["session_token"], test_id, "test_target"))
	#print(deleteVM(conf["api_base"], conf["session_token"], test_id))
	#test_resp = startVMProcess(conf["api_base"], conf["session_token"], test_id, guest_login, proc_spec)
	#print(test_resp)

def addHost(source_name, clone_name):
	resp = getVMIDs(conf["api_base"], conf["session_token"], source_name)
	#TODO - check getID success
		source_id = resp[0]["vm"]
		resp = cloneVM(conf["api_base"], conf["session_token"], source_id, clone_name)

		if(resp.status_code == 200):
			print("Adding host %s..." % clone_name)
			#write new host json
		else:
			print("Failed to add host %s" % clone_name)

#def removeHost(conf, host_name):
	resp = getVMIDs(conf["api_base"], conf["session_token"], host_name)
	host_id = resp[0]["vm"]
	#TODO - check getID success
		resp = deleteVM(conf["api_base"], conf["session_token"], host_id)
		if resp.status_code == 204:
			#remove host from hosts array
			#delete json file
		else:
			#print err


#def addVuln(conf, host_name, service):
	resp = getVMIDs(conf["api_base"], conf["session_token"], host_name)
	host_id = resp[0]["vm"]
	#TODO - check getID success
		resp = startVMProcess(conf["api_base"], conf["session_token"], host_id, guest_login)
