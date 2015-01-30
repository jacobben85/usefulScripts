import subprocess
import xml.etree.ElementTree as ET
import memcache

args = ["phantomjs", "pagevalidator.js", "http://www.univision.com"]
result = subprocess.check_output(args)

key = 'test'

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

mc.set(key, result, 60)
result = mc.get(key)

xmlTree = ET.ElementTree(ET.fromstring(result))

for url in xmlTree.iter('url'):
	print url.text