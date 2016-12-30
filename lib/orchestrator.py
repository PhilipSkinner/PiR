import httplib
import urllib
import json
import time

class Orchestrator():
    def __init__(self, name=None, type=None, params={}, orchestrator=None, port=None, logger=None):
        self.name = name
        self.type = type
        self.params = params
        self.orchestrator = orchestrator
        self.port = port
        self.logger = logger

        print "Starting to register with orchestrator..."

        while self.registerWithOrchestrator() == False:
            print "Waiting to register with orchestrator..."
            time.sleep(1)       

    def fetchConfigurationFromOrchestrator(self):
        #fetch our configuration from the orchestrator
        try:
            conn = httplib.HTTPConnection(self.orchestrator, port=self.port)
            conn.request(
                'GET',
                '/configuration/%s/%s' % (self.type, self.name)
            )

            response = conn.getresponse()

            if response.status == 200:
                data = json.loads(response.read())
                return data
        except:
            pass

        return None

    def downloadIRConfig(self, confName):
        try:
            conn = httplib.HTTPConnection(self.orchestrator, port=self.port)
            conn.request(
                'GET',
                '/configuration/file/%s' % (confName)
            )

            response = conn.getresponse()

            if response.status == 200:
                data = json.loads(response.read())
                print data            
        except:
            pass

        return None

    def registerWithOrchestrator(self):
        try:
            conn = httplib.HTTPConnection(self.orchestrator, port=self.port)
            conn.request(
                'POST', 
                '/register/%s/%s' % (self.type, self.name), 
                json.dumps(self.params),
                {
                    'Host' : self.orchestrator,
                    'Accept' : 'application/json, text/plain, */*',
                    'Content-Type' : 'application/json'
                })
            response = conn.getresponse()

            if response.status == 200:                
                data = json.loads(response.read())
                print "Registered with orchestrator!"
                return True
        except:
            pass

        print "Failed to register with orchestrator"
        return False                                    