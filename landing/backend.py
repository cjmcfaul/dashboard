import urllib3
import simplejson as json

api_key = 'UMBs_SY2DqqnILtSQJv60g2'
base_url = 'https://api.reply.io/v1/'

def get_campaigns():

    item = 'campaigns'

    url = '%s%s?apiKey=%s' % (base_url, item, api_key)

    http = urllib3.PoolManager()
    response = http.request('GET', url)

    json_items = json.loads(response.data)

    return json_items
