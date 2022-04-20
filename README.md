# red-team-deployment
Red Team deployment tool for UFSIT.


#### api_conf.json
A JSON file containing the API base and API account credentials must be located at './api_conf.json'. The session token is retrieved and stored by the tool, it should not be provided:

    {
        "api_base": "https://<API BASE>",
        "creds": {
            "user": "<API USERNAME>",
            "password": "<API PASSWORD>"
        },
        "session_token": ""
    }

  
#### hosts.json
A JSON file containing the list of hosts must be located at './hosts.json' with the following format:
    
    [{
        "id": "vm-XXXXX",
        "name": <HOST NAME>,
        "type": "<SOURCE VM ID>",
        "powered_on": false,
        "is_template": false
    }]

Hosts.json is managed by the tool and should not need editing or alteration.
If hosts.json is lost or corrupted, create a new hosts.json as follows with the hostnames that should be tracked:

    [{
        "id": "",
        "name": <HOST NAME 1>,
        "type": "",
        "powered_on": false,
        "is_template": false
    },
    {
        "id": "",
        "name": <HOST NAME 2>,
        "type": "",
        "powered_on": false,
        "is_template": false
    },
    {

        "id": "", 
        "name": "<HOST NAME 3>",
        "type": "", 
        "powered_on": false, 
        "is_template": false
    }]
  
Then start the tool and run the load command; details for each host will be populated from vCenter.
