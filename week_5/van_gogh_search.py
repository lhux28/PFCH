import requests
import json

url = 'https://collectionapi.metmuseum.org/public/collection/v1/search'
#API endpoint -- search feature

url_parameters = {
    "artistOrCulture": "true",
    "isOnView": "true",
    "hasImages": "true",
    "q": "van_gogh"
}
#search for Vincent Van Gogh in the ArtistsOrCulture key, 
#and is on view, and has image

met_api_request = requests.get(url, params=url_parameters)
#request data from api -- link together the url and parameters
#is saying this: 'https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&isOnView=true&hasImages=true&q=vincent_van_gogh'

json_data = json.loads(met_api_request.text)
#make the data from the endpoint readable as a dictionary

print(json.dumps(json_data, indent=2))