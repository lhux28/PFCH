import requests
import cloudscraper
from bs4 import BeautifulSoup
import time
#Get all the tools i need

base_url = 'https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86&page='
#set variable for the source of my data

dict_list = []

page_num = 0
while 0 <= page_num < 3:
    time.sleep(0.25)
    scraper = cloudscraper.create_scraper()
    page = scraper.get(f'{base_url}{page_num}')
    page_num += 1
    #set cloudscraper instance and scrape the 3 pages on website
    # print(page.text)

    soup = BeautifulSoup(page.text, 'html.parser')
    #run script through beautiful soup so i can use all the tools in their lib
    # print(soup.prettify())

    grid_item_content = soup.find_all("div", {'class': 'grid__content'})
    #find all the divs where artworks are
    # print(grid_item_content)
    # print(len(grid_item_content))

    for artwork_div in grid_item_content:
        time.sleep(0.25)
        artwork_title = artwork_div.find('p')
    #find pic, title, artist for each artwork
    # print(artwork_title)

        artist = artwork_div.find('a', {'class': 'card__title-link'}).text.strip()
        #grab all artist names

        for href in artwork_title:
            time.sleep(0.25)
            url_tail = href.get('href')
        #find the url tail of each one
        # print(url_tail)

            artwork_url = f"https://www.phillipscollection.org{url_tail}"
            # print(artwork_url)

            artwork_page = scraper.get(artwork_url)
            # print(artwork_page.text)

            soup = BeautifulSoup(artwork_page.text,'html.parser')
            # print(artwork_soup.prettify)

            metadata_div = soup.find_all('ul', {'class': 'collection-meta flex-layout__item'})
            # print(metadata_div)


            for material_span in metadata_div:
                time.sleep(0.25)
                material_label = material_span.find_next("span", {'collection-meta__type'}, string='Materials')
                # print(material_label)
                
                if material_label:
                    material = material_label.find_next("span", {'collection-meta__value'})
                    # print(material)

            
            for dimension_span in metadata_div:
                time.sleep(0.25)
                dimension_label = dimension_span.find_next("span", {'collection-meta__type'}, string='Dimensions')
                # print(dimension_label)
                
                if dimension_label:
                    dimensions = dimension_label.find_next("span", {'collection-meta__value'})
                    # print(dimensions)

            art_dict = {
                'artist': artist,
                'material': material.text.strip(),
                'dimensions': dimensions.text.strip()
            }

                    # print(art_dict)
            dict_list.append(art_dict)


# print(dict_list)
print(len(dict_list))
        


# steps:
    #go through each page
    #find where the artwork_title titles are
    #create loop to go through each record to fetch names
    #with each name > go to page
    #make a dictionary for each object > {'artist': 'name', 'material': 'oil', 'dimensions': '1cm.'}
    #append to array