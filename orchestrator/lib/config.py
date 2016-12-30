import ConfigParser
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser.RawConfigParser()

def _readDevicesFile():
    config.read('%s/../config/devices.conf' % dir_path)    

def readOrchestratorConfig():
    config.read('%s/../config/orchestrator.conf' % dir_path)

    raw = config.options('orchestrator')
    ret = {}    

    for arg in raw:
        ret[arg] = config.get('orchestrator', arg)

    return ret

def readIRDevices():       
    _readDevicesFile()

    #generate a simple list of the devices    
    devicesRaw = config.options('lircdevices')

    raw = {}
    ret = {}

    for dev in devicesRaw:
        raw[dev] = config.get('lircdevices', dev)

    for k, v in raw.iteritems():
        if os.path.isfile('%s/../config/lirc/%s.conf' % (dir_path, v)):
            ret[k] = v    

    return ret

def readNodeDevices():
    _readDevicesFile()

    #we need our IR devices
    irDevices = readIRDevices()

    nodesRaw = config.options('irnodes')

    ret = {}

    for dev in nodesRaw:
        ret[dev] = {}

        #read this nodes conf section        
        nodeConf = config.options(dev)

        for toControl in nodeConf:            
            if toControl in irDevices:
                ret[dev][toControl] = irDevices[toControl]

    return ret