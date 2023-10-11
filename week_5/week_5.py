import json
counter = {}

with open('Artworks.json', 'r') as file:
    art_read_file = json.load(file)
    for artwork in art_read_file:
        nat_list = artwork["Nationality"]
        for nat in nat_list:
            if counter.get(nat) is None:
            #looks at counter dictionary and sees if nat is in there, if not..
                with open(f'res/{nat}.json', 'w') as nat_file:
                #make file for nationality
                    writer = json.dump(artwork, nat_file, indent=2)
                    #copies artwork rows from Artworks.json, puts it into a file
                    #dump rather than dumps because it is already in json format
                    counter[nat] = True
            else:
                with open(f'res/{nat}.json', 'a') as nat_file:
                    writer = json.dump(artwork, nat_file, indent=2)
