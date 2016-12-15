import httplib
import urllib
import json

class API():
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.login()
        
    def getConnection(self):
        return httplib.HTTPSConnection("beekeeper.hivehome.com")

    def login(self):
        print json.dumps({
            'username' : self.username,
            'password' : self.password
        })

        conn = self.getConnection()
        conn.request('POST', '/1.0/gateway/login', json.dumps({
            'username' : self.username,
            'password' : self.password
        }), {
            'Host' : 'beekeeper.hivehome.com',          
            'Accept' : 'application/json, text/plain, */*',
            'Content-Type' : 'application/json',
        })

        response = conn.getresponse()
        print response.status
        print response.read()
        
        if response.status != 200:
            return False
        
        return True