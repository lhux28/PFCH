import csv
counter = {}

with open('Artworks.csv', 'r') as file:
    art_read_file = csv.DictReader(file)
    for artwork in art_read_file:
        nat_list = artwork["Nationality"].split(" ") #why does it come back as multiple single lists rather than one continuous one?
        for nat in nat_list:
            if counter.get(nat) is None:
                with open(f'res/{nat}.csv', 'w') as nat_file:
                    writer = csv.DictWriter(nat_file, fieldnames=art_read_file.fieldnames)
                    writer.writeheader()
                    writer.writerow(artwork)
                    counter[nat] = True
            else:
                with open(f'res/{nat}.csv', 'a') as nat_file:
                    writer = csv.DictWriter(nat_file, fieldnames=art_read_file.fieldnames)
                    writer.writerow(artwork)