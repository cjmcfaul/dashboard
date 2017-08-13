import urllib3
import simplejson as json
import http.client, urllib.request, urllib.parse, urllib.error, base64

<<<<<<< HEAD
reply_api_key = 'UMBs_SY2DqqnILtSQJv60g2'
reply_base_url = 'https://api.reply.io/v1/'

transit_api_key = '3833947c624b4eef9eccf542b4740213'
transit_base_url = 'api.wmata.com'
=======
api_key = '''put a reply.io api key in here'''
base_url = 'https://api.reply.io/v1/'
>>>>>>> 5b31e41378d818e11933b3ad8f5b3b2c6dcbc3b9

def get_campaigns():

    item = 'campaigns'

    url = '%s%s?apiKey=%s' % (reply_base_url, item, reply_api_key)

    http = urllib3.PoolManager()
    response = http.request('GET', url)

    json_items = json.loads(response.data)

    return json_items

def get_bus_predic(stop_id):

    headers = {
        # Request headers
        'api_key': transit_api_key,
    }

    params = urllib.parse.urlencode({
        'StopID': stop_id,
    })

    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/NextBusService.svc/json/jPredictions?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    json_items = json.loads(data)

    return json_items

def get_train_predic(station_code):

    headers = {
        # Request headers
        'api_key': transit_api_key,
    }

    url = "/StationPrediction.svc/json/GetPrediction/%s?" % (station_code)

    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", url, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    json_items = json.loads(data)

    print(json_items)

    return json_items
