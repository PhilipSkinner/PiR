import ConfigParser
import os

config = ConfigParser.RawConfigParser()

def readNodeConfig(dir):    
    config.read('%s/node.conf' % dir)

    ret = {
        'node'         : {},
        'orchestrator' : {}
    }

    nodeRaw = config.options('node')

    for arg in nodeRaw:
        ret['node'][arg] = config.get('node', arg)    

    orchestratorRaw = config.options('orchestrator')

    for arg in orchestratorRaw:
        ret['orchestrator'][arg] = config.get('orchestrator', arg)

    return ret