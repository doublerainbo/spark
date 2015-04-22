'''
Created on Apr 4, 2015

@author: doublerainbo
'''

import urllib2, json, base64


class APIClient:
    def __init__(self, base_url):
        self.username = ''
        self.password = ''
        self.accesskey = ''
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url

    #
    # Send Get
    #
    # Issues a GET request (read) against the API and returns the result
    # (as Python dict).
    #
    # Arguments:
    #
    # uri                 The API method to call including parameters
    #                     (e.g. get_case/1)
    #
    def send_get(self, uri):
        return self.__send_request('GET', uri, None)

    #
    # Send POST
    #
    # Issues a POST request (write) against the API and returns the result
    # (as Python dict).
    #
    # Arguments:
    #
    # uri                 The API method to call including parameters
    #                     (e.g. add_case/1)
    # data                The data to submit as part of the request (as
    #                     Python dict, strings must be UTF-8 encoded)
    #
    def send_post(self, uri, data):
        return self.__send_request('POST', uri, data)

    def get_access_key(self, data):
        url = "https://www.spark.io/sign-in"
        request = urllib2.Request(url)
        
        request.add_header('Content-Type', 'application/json')
        request.add_data(json.dumps(data))
        e = None
        try:
            response = urllib2.urlopen(request).read()
        except urllib2.HTTPError as e:
            response = e.read()

        if response:
            result = json.loads(response)
        else:
            result = {}

        if e != None:
            if result and 'error' in result:
                error = '"' + result['error'] + '"'
            else:
                error = 'No additional error message received'
            raise APIError('API returned HTTP %s (%s)' % 
                (e.code, error))

        return result['auth_token']
        
#         Authentication POST to https://www.spark.io/sign-in15 Headers: Content-Type: application/json
# Body: {"username":"youremailaddress","password":"spark_password"}

        
    def __send_request(self, method, uri, data):
        url = self.__url + uri
        request = urllib2.Request(url)
        
        if (method == 'POST'):
            request.add_data(json.dumps(data))
        
        if self.accesskey == '':
            #auth = base64.encodestring('%s:%s' % (self.username, self.password)).strip()
            #request.add_header('Authorization', 'Basic c3Bhcms6c3Bhcms=')
            #request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            
            self.access_key = self.get_access_key({"username": self.username, "password": self.password })
            

        auth = self.accesskey
        request.add_header('Authorization', 'Bearer %s' % auth)
        request.add_header('Content-Type', 'application/json')
        request.add_header('Accept', 'application/json')

        e = None
        try:
            response = urllib2.urlopen(request).read()
        except urllib2.HTTPError as e:
            response = e.read()

        if response:
            result = json.loads(response)
        else:
            result = {}

        if e != None:
            if result and 'error' in result:
                error = '"' + result['error'] + '"'
            else:
                error = 'No additional error message received'
            raise APIError('API returned HTTP %s (%s)' % 
                (e.code, error))

        return result

class APIError(Exception):
    pass

def login():
    client = APIClient("https://api.spark.io/")
    #client.username = "spark"
    #client.password = "spark"
    client.username = "bozhao12@gmail.com"
    client.password = "cowsgomoo"
    
    # request a token
#     tokenResp = client.send_post("oauth/token", {"grant_type": "password", 
#                                                  "username": client.username, 
#                                                  "password" : client.password })
    
    
    #client.accesskey = tokenResp["access_token"]
    return client
