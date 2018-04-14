import urllib2
content = urllib2.urlopen(some_url).read()
print content

import httplib
conn = httplib.HTTPConnection("www.python.org")
conn.request("HEAD","/index.html")
res = conn.getresponse()
print res.status, res.reason
# Result:
200 OK

import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
# Result:
200


## What a POST and GET Function Coud Look Like ##

import requests
url = 'https://...'
payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get(url)

# GET with params in URL
r = requests.get(url, params=payload)

# POST with form-encoded data
r = requests.post(url, data=payload)

# POST with JSON
import json
r = requests.post(url, data=json.dumps(payload))

# Response, status etc
r.text
r.status_code
