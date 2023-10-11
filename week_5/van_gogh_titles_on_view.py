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

met_api_search = requests.get(url, params=url_parameters)
#request data from api -- link together the url and parameters
#is saying this: 'https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&isOnView=true&hasImages=true&q=vincent_van_gogh'

json_data = json.loads(met_api_search.text)
#make the data from the endpoint readable as a dictionary

object_ids = json_data['objectIDs']
#find objectids 
#object_ids is a list: [459123, 437984, 436532,...]

title_list = []
for object in object_ids:
#loop through each objectID
    obj_url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object}'
    #attach object id to end of url
    met_api_object = requests.get(obj_url)
    #request data
    object_data = json.loads(met_api_object.text)
    #make data parsable in json
    object_title = object_data["title"]
    #retrieve title for the object
    title_list.append(object_title)
    #add it to the list

print(title_list)
