import hashlib
import base64
import urllib
import time
import json


class ooyala_api(object):
    def generate_signature(self, secret_key, http_method, request_path, query_params, request_body=''):
        signature = secret_key + http_method.upper() + request_path

        for key, value in query_params.iteritems():
            signature += key + '=' + value

        print signature
        signature = base64.b64encode(hashlib.sha256(signature).digest())[0:43]
        signature = urllib.quote_plus(signature)

        return signature

    def fetch_video_metadata(self, providerId, signature, expires):
        url = 'https://cdn-api.ooyala.com/v2/assets?api_key=RvYzg6W4ZZ2OMccHJ_SNtCIZCrg6.Muak6&where=metadata.providerId=' + providerId + '&signature=' + signature + '&expires=' + expires

        print url

        response = urllib.urlopen(url)

        jsonObject = json.load(response)
        print jsonObject


# Example usage of the generate_signature function:
# Example URL : http://api.ooyala.com/docs/v2/ 
new_ooyala_api = ooyala_api()
expires = str(int(time.time() + 24 * 3600))
query_params = {'api_key': 'RvYzg6W4ZZ2OMccHJ_SNtCIZCrg6.Muak6', 'expires': expires}

signature = new_ooyala_api.generate_signature('hgeZOk1ZnGSDa8BSn3-VK0LHNqJ2o521SokWF-VF', 'get', 'assets', query_params)

print signature

new_ooyala_api.fetch_video_metadata('3020147', signature, expires)

time.sleep(20)
new_ooyala_api.fetch_video_metadata('3020147', signature, expires)
