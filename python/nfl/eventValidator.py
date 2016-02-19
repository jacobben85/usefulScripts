import json
import xml.etree.ElementTree as ET
import urllib2
import urllib
import requests
import time
import subprocess

eventXML = 'http://nfl.univision.com/feed/sports/american-football/nfl/2014/event-nfl-56498.xml'


def validate(eventXML):
    response = requests.get(eventXML)

    if response.status_code == 200:

        if response.headers['Content-Type'].find('xml') > -1:
            urllib.urlretrieve(eventXML, '/tmp/event.xml')
            xmlData = ET.parse('/tmp/event.xml')

            for node in xmlData.iter('response'):
                status = node.attrib.get('status')
                if status != 'success':
                    statusCheck = 'Status:fail, Type:XML'
                else:
                    statusCheck = 'Status:success, Type:XML'

        subprocess.check_call(
            ['/usr/bin/osascript', '-e', 'display notification "' + statusCheck + '" with title "MoGreet Validator"'])


n = 300
while n > 0:
    validate(eventXML)
    n = n - 1
    time.sleep(60)
