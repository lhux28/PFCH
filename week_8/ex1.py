import requests
import cloudscraper
from bs4 import BeautifulSoup
import time
#Get all the tools i need

base_url = 'https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86&page='
#set variable for the source of my data

artwork_list = []

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
        artwork_title = artwork_div.find('p').text.strip()

        # print(artwork_title)

        artwork_list.append(artwork_title)
    #loop through all divs in grid to find all the title
    #add them to list

print(artwork_list)
# print(len(artwork_list))

# steps:
    #go through each page
    #find where the artwork_title titles are
    #create loop to go through each record to fetch names
    #append to array