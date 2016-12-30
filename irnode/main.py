import os
import sys

#fix the relative import issues
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)

from node import node
from lib import orchestrator

if __name__ == '__main__':
    conf = node.config.readNodeConfig(os.path.dirname(os.path.realpath(__file__)))        

    #register ourselves with the orchestrator
    parent = orchestrator.Orchestrator(
        name = conf['node']['name'], 
        type = 'irnode', 
        params = {
            'address'   : conf['node']['address'],
            'port'      : conf['node']['port']
        },
        orchestrator = conf['orchestrator']['address'],
        port = conf['orchestrator']['port'],
        logger = node.app.logger)    

    #get our configuration from the orchestrator
    remoteConfig = parent.fetchConfigurationFromOrchestrator()

    if 'devices' in remoteConfig:        
        node.devices = remoteConfig['devices']    

    #for each device we are to control, we need to download the conf
    #file from the orchestrator
    for k, v in node.devices.iteritems():
        print "Downloading %s config for device %s" % (v, k)
        parent.downloadIRConfig(v, conf['lirc']['config'])

    if remoteConfig != None:
        node.app.run(host=conf['node']['address'], port=int(conf['node']['port']), debug=True)