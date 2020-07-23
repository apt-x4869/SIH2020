import os

import requests

#from .root import app


base_url_photos = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="
api_key = os.environ['API_KEY']

#@app.handle(intent='search_places')
def search_places (request, responder ) :
    #place = get_place(request)
    place = 'Ranchi'
    url = construct_url(place)
    print(url)

def construct_url(place):
    base_url = "https://maps.googleapis.com/maps/api/place/"
    url1 = "findplacefromtext/json?input="
    url2 = "&inputtype=textquery&fields=photos,formatted_address,name,geometry,place_id&key="
    url_string = base_url + url1 + place + url2 + str(api_key)
    return url_string

search_places('c','b')