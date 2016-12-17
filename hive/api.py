import httplib
import urllib
import json
import devices.light

class API:
    def __init__(self, username, password):        
        self.username = username
        self.password = password
        self.token = None
        self.lights = []

        self.login()
        self.getLights()   

    def setBrightness(self, id, value):
        conn = self.getAPIConnection()
        conn.request('PUT', '/omnia/nodes/%s' % id, json.dumps({
            "nodes" : [
                {
                    "attributes" : {
                        "brightness" : {
                            "targetValue" : value
                        }
                    }
                }
            ]            
        }), {
            'Host' : 'api-prod.bgchprod.info',
            'Accept' : 'application/vnd.alertme.zoo-6.4+json',
            'X-AlertMe-Client' : 'Hive Web Dashboard',
            'Content-Type' : 'application/json',
            'X-Omnia-Access-Token' : self.token
        })

        response = conn.getresponse()        

        if response.status != 200:
            return False            
        
        return True 

    def lightOff(self, id):
        conn = self.getAPIConnection()
        conn.request('PUT', '/omnia/nodes/%s' % id, json.dumps({
            "nodes" : [
                {
                    "attributes" : {
                        "state" : {
                            "targetValue" : "OFF"
                        }
                    }
                }
            ]            
        }), {
            'Host' : 'api-prod.bgchprod.info',
            'Accept' : 'application/vnd.alertme.zoo-6.4+json',
            'X-AlertMe-Client' : 'Hive Web Dashboard',
            'Content-Type' : 'application/json',
            'X-Omnia-Access-Token' : self.token
        })

        response = conn.getresponse()        

        if response.status != 200:
            return False            
        
        return True
    
    def lightOn(self, id):
        conn = self.getAPIConnection()
        conn.request('PUT', '/omnia/nodes/%s' % id, json.dumps({
            "nodes" : [
                {
                    "attributes" : {
                        "state" : {
                            "targetValue" : "ON"
                        }
                    }
                }
            ]            
        }), {
            'Host' : 'api-prod.bgchprod.info',
            'Accept' : 'application/vnd.alertme.zoo-6.4+json',
            'X-AlertMe-Client' : 'Hive Web Dashboard',
            'Content-Type' : 'application/json',
            'X-Omnia-Access-Token' : self.token
        })

        response = conn.getresponse()

        if response.status != 200:
            return False
        
        return True
        
    def getLights(self):
        #get a list of all of our lights
        conn = self.getAPIConnection()
        conn.request('GET', '/omnia/nodes', '', {
            'Host' : 'api-prod.bgchprod.info',
            'Accept' : 'application/vnd.alertme.zoo-6.4+json',
            'X-AlertMe-Client' : 'Hive Web Dashboard',
            'X-Omnia-Access-Token' : self.token
        })

        response = conn.getresponse()

        if response.status != 200:
            return

        data = json.loads(response.read())
        
        for node in data['nodes']:            
            #is it a light?
            if node['nodeType'] == 'http://alertme.com/schema/json/node.class.light.json#':
                #yes, init a light object from this node
                self.lights.append(devices.light.HiveLight(node))
                

    def getAuthConnection(self):
        return httplib.HTTPSConnection("beekeeper.hivehome.com")

    def getAPIConnection(self):
        return httplib.HTTPSConnection("api-prod.bgchprod.info")

    def login(self):
        conn = self.getAuthConnection()
        conn.request('POST', '/1.0/gateway/login', json.dumps({
            'username' : self.username,
            'password' : self.password
        }), {
            'Host' : 'beekeeper.hivehome.com',          
            'Accept' : 'application/json, text/plain, */*',
            'Content-Type' : 'application/json',
        })

        response = conn.getresponse()                
        
        if response.status != 200:
            return False

        data = json.loads(response.read())

        #get our access token
        self.token = data['token']
        
        return True