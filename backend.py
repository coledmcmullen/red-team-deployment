#backend.py

from api_calls import *

#API configuration file relative path
conf_path = "./api_conf.json"
guest_creds = {
	"interactive_session": True,
	"password": "ufcptc2020!",
	"type": "USERNAME_PASSWORD",
	"user_name": "ufcptc"
}
proc_spec = {
	#"path": "/usr/bin/top"
	"path": "/usr/lib/firefox-esr/firefox-esr"
}

def init():
	conf = loadConf(conf_path)
	conf["session_token"] = getSessionToken(conf["api_base"], conf["creds"])
	return conf

def testCalls():
	conf = init()
	test_resp = getVMIDs(conf["api_base"], conf["session_token"], ["test_kali"])
	test_id = test_resp[0]["vm"]
	#test_resp = listVMFolder(conf["api_base"], conf["session_token"], ["Spring_2022_Laforge_Senior_Project"])
	print(test_resp)
	print(test_id)
	#print(getVMInfo(conf["api_base"], conf["session_token"], test_id))
	#print(getVMInfo(conf["api_base"], conf["session_token"], ["rtdt_live"]))
	#print(powerOffVM(conf["api_base"], conf["session_token"], test_id))
	#print(powerOnVM(conf["api_base"], conf["session_token"], test_id))
	#print(cloneVM(conf["api_base"], conf["session_token"], test_id, "test2_kali"))
	#print(deleteVM(conf["api_base"], conf["session_token"], test_id))
	test_resp = startVMProcess(conf["api_base"], conf["session_token"], test_id, guest_creds, proc_spec)
	print(test_resp)

#def addHost():


#def addVuln():
