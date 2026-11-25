import json
import re
#make sure you install serpapi and dotenv modules by running  below code 
pip install google-search-results
pip install python-dotenv
pip install serpapi
import time
import requests
import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

#Add Serpapi API key to .env with as "SERPAPI_API_KEY"
SERPAPI_API = os.getenv('SERPAPI_API_KEY')

#Enter the search query for images
search_query = 'box at front door'
google_search_api = f'https://serpapi.com/search.json?q={search_query}&engine=google_images&ijn=0&api_key=de63787718779ac922fccc35fd4e4c8ee1c61d1e2ae171f83ec2db1299c98075'
res = requests.get(url = google_search_api, headers={'Authorization': SERPAPI_API})
data = res.json()

def extract_url_from_google(json):
    k=0
    url_list = []
    while k != 90:
        original_url = json['images_results'][k]['original']
        url_list.append(original_url)
        k = k+1
    
    return url_list

#Extracting image urls from data object
image_urls = extract_url_from_google(data)

directory_name = 'boxes'.replace(" ", "_")
#if boxes directory doesn't exsist then making one named 'boxes'
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

# download and save the specified number of images to the directory*0
i=0
for url in image_urls:
   try:
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the filename from the URL
        filename = url.split("/")[-1]
        # Save the image to the specified directory
        save_path = os.path.join(directory_name, filename)

        with open(f'{directory_name}/image_{i+1}.jpg', "wb") as file:
            file.write(response.content)
            print(f"Image saved: {save_path}")
            i = i+1
            time.sleep(2)
    else:
        print(f"Failed to download image from URL: {url}")
   except:
    continue
   
