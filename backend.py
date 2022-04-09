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
	print(getVMList(conf["api_base"], conf["session_token"]))

