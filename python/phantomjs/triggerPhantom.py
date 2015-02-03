import subprocess
import xml.etree.ElementTree as ET
import memcache
import hashlib
from Queue import Queue


class CacheMemcached:
    """Memcached cache service class
    to be updated referring to
    http://blog.echolibre.com/2009/11/memcache-and-python-getting-started/"""
    cacheInstance = False

    def __init__(self, host='127.0.0.1', port='11211'):
        self.status = False
        self.host = host
        self.port = port
        if self.memcached_service_status():
            CacheMemcached.cacheInstance = memcache.Client([host + ':' + port], debug=0)

    def get_instance(cls):
        if cls.status:
            return cls.cacheInstance;
        else:
            return False
    
    def memcached_service_status(self):
        try:
            checkService = subprocess.check_output("ps aux | grep '[m]emcached'", shell=True)
            if len(checkService.splitlines()) > 0:
                self.status = True
        except:
            self.status = False
        finally:
            return self.status
        return self.status

    def get_from_cache_store(cls, key):
        result_set = False
        if cls.status:
            result_set = cls.cacheInstance.get(key)
            if result_set is None:
                result_set = False

        return result_set

    def set_to_cache(cls, key, values):
        result_set = False
        if cls.status:
            result_set = cls.cacheInstance.set(key, values, 0)

        return result_set

    def generate_key_from_string(cls, url):
        m = hashlib.md5()
        m.update(url)
        return m.hexdigest()


class PhantomJsWrapper:
    """Phantom JS wrapper"""
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
    

def url_processor(url_q, processed_list, mc):

    url_org = url_q.get()

    if mc.memcached_service_status is False:
        return

    key = mc.generate_key_from_string(url_org)

    result = mc.get_from_cache_store(key)

    try:
        if processed_list.index(key) < 0:
            processed_list.append(key)
    except ValueError:
        processed_list.append(key)

    urlList = False

    if result is False:
        urlList = PhantomJsWrapper().get_urls(url_org)
        result = {'count': 1, 'processed': True, 'tries': 0, 'url': url_org}
    elif result['processed'] is True:
        result = {'count': result['count'] + 1, 'processed': True, 'tries': result['tries'], 'url': url_org}
    elif result['tries'] < 2:
        urlList = PhantomJsWrapper().get_urls(url_org)
        result = {'count': result['count'] + 1, 'processed': True, 'tries': result['tries'], 'url': url_org}
    else:
        result = {'count': result['count'] + 1, 'processed': True, 'tries': result['tries'], 'url': url_org}

    if urlList is not False:
        try:
            xmlTree = ET.ElementTree(ET.fromstring(urlList))
            for url in xmlTree.iter('url'):
                url_q.put(url.text)

            result = {'count': result['count'], 'processed': True, 'tries': result['tries'] + 1, 'url': url_org}
        except:
            print "except : " + url_org
            result = {'count': result['count'] - 1, 'processed': False, 'tries': result['tries'] + 1, 'url': url_org}
            url_q.put(url_org)
        finally:
            mc.set_to_cache(key, result)
    else:
        mc.set_to_cache(key, result)


url_q = Queue()
url = "http://www.univision.com"
url_q.put(url)
processed_list = []
mc = CacheMemcached()


while not url_q.empty():
    url_processor(url_q, processed_list, mc)

print 'urls : ' + str(len(processed_list))

for key in processed_list:
    print mc.get_from_cache_store(key)

mc.get_instance().flush_all()
