#backend.py

from api_calls import *

#API configuration file relative path
conf_path = "./api_conf.json"

def init():
	conf = loadConf(conf_path)
	conf["session_token"] = getSessionToken(conf["api_base"], conf["creds"])
	return conf

def testCalls():
	conf = init()
	test_id = getVMList(conf["api_base"], conf["session_token"], ["test2_kali"])[0]["vm"]
	print(test_id)
	#print(getVMInfo(conf["api_base"], conf["session_token"], test_id))
	#print(powerOffVM(conf["api_base"], conf["session_token"], test_id))
	#print(powerOnVM(conf["api_base"], conf["session_token"], test_id))
	#print(cloneVM(conf["api_base"], conf["session_token"], test_id, "test2_kali"))
	print(deleteVM(conf["api_base"], conf["session_token"], test_id))

