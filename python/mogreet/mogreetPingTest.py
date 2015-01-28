#!/usr/local/bin/python
import json
import xml.etree.ElementTree as ET
import urllib2
import urllib
import requests
#import schedule
import random
import time
import subprocess

mogreeturl = 'http://www-test.uim.univision.com/mogreetConduit.do?isTest=1'

def validate(mogreeturl):
    
    randNumber = random.randint(1,2)
    statusCheck = 'status:fail, type:xml'
    
    if randNumber == 2:
        mogreeturl = mogreeturl + '&format=JSON'
    
    response = requests.get(mogreeturl)
    
    if response.status_code == 200:
        if response.headers['Content-Type'].find('json') > -1:
    
            data = urllib2.urlopen(mogreeturl)
            jsonData = json.loads(data.read())
    
            if jsonData['response']['status'] != 'success':
                statusCheck = 'Status:fail, Type:JSON'
            else:
                statusCheck = 'Status:success, Type:JSON'
    
        elif response.headers['Content-Type'].find('xml') > -1:
            urllib.urlretrieve (mogreeturl, '/tmp/mogreet.xml')
            xmlData = ET.parse('/tmp/mogreet.xml')
    
            for node in xmlData.iter('response'):
                status = node.attrib.get('status')
                if status != 'success':
                    statusCheck = 'Status:fail, Type:XML'
                else:
                    statusCheck = 'Status:success, Type:XML'
        
        subprocess.check_call(['/usr/bin/osascript', '-e', 'display notification "' + statusCheck + '" with title "MoGreet Validator"'])

n = 300
while n > 0:
    validate(mogreeturl)
    n = n-1
    time.sleep(60)
    
