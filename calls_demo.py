#!/usr/bin/python3

import requests
#import logging

api_base = 'https://<ENDPOINT BASE URL>'
api_uname = '<API USERNAME>'
api_pass = '<API PASSWORD>'

#logging.captureWarnings(True)

sess = requests.post('{}/api/session'.format(api_base), auth=(api_uname, api_pass), verify=True)
session_id = sess.json()

print(sess.status_code)
print(session_id)
print(sess.elapsed)

resp = requests.get('{}/api/vcenter/vm'.format(api_base), verify=True, headers={
    "vmware-api-session-id": session_id
})

#print(u"resp.text = %s" % str(resp.text))
#print(sess.json())
print(resp.json())
