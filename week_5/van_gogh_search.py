import requests
import json

url = 'https://collectionapi.metmuseum.org/public/collection/v1/search'
#API endpoint -- search feature

url_parameters = {
    "artistOrCulture": "true",
    "isOnView": "true",
    "hasImages": "true",
    "q": "vincent_van_gogh"
}
#search for Vincent Van Gogh in the ArtistsOrCulture key, 
#and is on view, and has image

met_api_request = requests.get(url, params=url_parameters)
#request data from api -- link together the url and parameters
#is saying this: 'https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&isOnView=true&hasImages=true&q=vincent_van_gogh'

json_data = json.loads(met_api_request.text)
#make the data from the endpoint readable as a dictionary

object_ids = json_data['objectIDs']
#find objectids 
#object_ids is a list: [459123, 437984, 436532,...]

print(json.dumps(object_ids, indent=2))
#pretty print in json