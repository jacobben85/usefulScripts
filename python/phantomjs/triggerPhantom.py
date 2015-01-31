import subprocess
import xml.etree.ElementTree as ET
import memcache


class CacheMemecached:
    'Memcached cache service class'
    cacheInstance = False

    def __init__(self, host, port):
        self.status = False
        self.host = host
        self.port = port
        if self.memcache_service_status():
            CacheMemecached.cacheInstance = memcache.Client([host + ':' + port], debug=0)

    def get_instance(cls):
        if cls.status:
            return cls.cacheInstance;
        else:
            return False
    
    def memcache_service_status(self):
        try:
            checkService = subprocess.check_output("ps aux | grep '[m]emcached'", shell=True)
            if len(checkService.splitlines()) > 0:
                self.status = True
        except:
            self.status = False
        finally:
            return self.status
        return self.status


class PhantomJsWrapper:
    def __init__(self):
        self.args = ["phantomjs", "pagevalidator.js"]
        self.response = False
        
    def get_urls(self, url):
        self.args = self.args + [url]
        self.get_response()
        return self.response
        
    def get_response(self):
        try:
            self.response = subprocess.check_output(self.args)
        except:    
            self.response = False
    

#args = ["phantomjs", "pagevalidator.js", "http://www.univision.com"]
result = PhantomJsWrapper().get_urls("http://www.univision.com")

key = 'test'

mc = CacheMemecached('127.0.0.1', '11211').get_instance()

if mc != False:
    mc.set(key, result, 60)
    result = mc.get(key)
    print 'set and get from cache'
else:
    print 'memcache not found'
    
if result != False:
    xmlTree = ET.ElementTree(ET.fromstring(result))

    for url in xmlTree.iter('url'):
            print url.text