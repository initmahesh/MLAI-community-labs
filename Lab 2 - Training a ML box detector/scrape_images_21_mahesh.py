import os
import requests
from bs4 import BeautifulSoup
def download_images_from_google_search(search_string, num_images):
    # format the search string for Google search
    formatted_search_string = search_string.replace(" ", "+")
    url = f"https://www.google.com/search?q={formatted_search_string}&tbm=isch"
    # send a request to the URL and get the HTML response
    response = requests.get(url)
    html = response.content
    # parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # find all the image elements on the page
    image_elements = soup.findAll('img')
    # extract the image URLs from the image elements
    image_urls = [img['src'] for img in image_elements]
    # create a directory to save the images
    directory_name = search_string.replace(" ", "_")
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    # download and save the specified number of images to the directory
    for i, url in enumerate(image_urls[:num_images]):
        try:
            response = requests.get(url)
            with open(f'{directory_name}/image_{i+1}.jpg', 'wb') as f:
                f.write(response.content)
                print(f"download image {i+1}")
        except:
            print(f"Could not download image {i+1}")
# example usage: download the first 10 images for "box on door steps"
download_images_from_google_search("box on door steps", 10)