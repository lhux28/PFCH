import requests
import json

url = 'https://collectionapi.metmuseum.org/public/collection/v1/search'
#API endpoint -- search feature

# url_parameters = {
#     "isOnView": "true",
#     "hasImages": "true",
#     "q": "van gogh"
# }

met_api_request = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?q=van gogh&isOnView=true&hasImages=true')
#request data from api -- link together the url and parameters

json_data = json.loads(met_api_request.text)
#make the data from the endpoint readable as a dictionary

print(json.dumps(json_data, indent=2))