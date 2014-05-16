import requests
import json

YAHOO_ID = 'insert your ID'

def getWOEID(location):
    if not location:
        return 'nolocation'

    url = 'http://where.yahooapis.com/v1/places.q(\'%s\')?appid=%s&format=json' % (
        location, YAHOO_ID
    )

    r = requests.get(url)
    json = r.json()
    places = json['places']

    if not places['count']:
        return 'noplaces'

    place = places['place'][0]

    return place['woeid']
