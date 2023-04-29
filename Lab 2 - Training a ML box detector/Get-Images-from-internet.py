
import os
import requests
from bs4 import BeautifulSoup
"""
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
download_images_from_google_search("images with multiple screen shots of apple phone app screen", 40)
"""
###AIzaSyCBadf7bXudnnlAUvbOVQCGnwfnHkrSCOk

API_KEY = "AIzaSyCBadf7bXudnnlAUvbOVQCGnwfnHkrSCOk"
SEARCH_ENGINE_ID = "a2825b95453084db6"

def get_image_urls_from_google_api(search_string, num_images):
    # format the search string for Google API
    formatted_search_string = search_string.replace(" ", "+")
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={formatted_search_string}&searchType=image&num={num_images}"

    # send a request to the Google API and get the JSON response
    response = requests.get(url)
    json_data = response.json()

    # extract the image URLs from the JSON response
    #image_urls = [item['link'] for item in json_data['items']]

    # extract the image URLs from the JSON response
    image_urls = []
    try:
        for item in json_data['items']:
            try:
                link = item['link']
                image_urls.append(link)
            except KeyError:
                # 'link' key doesn't exist in this item
                print("Could not find 'link' key in an item.")
    except KeyError:
        # 'items' key doesn't exist in the JSON data
        print("Could not find 'items' key in the JSON data.")
        return image_urls

    return image_urls

num_images=10
search_string="imahes of app screen with multple screen shots"
# example usage: get the first 10 image URLs for "box on door steps"
image_urls = get_image_urls_from_google_api(search_string, num_images)
#print(image_urls)

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

"""
import requests
from bs4 import BeautifulSoup
import os

def download_images(search_string, num_images):
    # format the search string for Bing search
    formatted_search_string = search_string.replace(" ", "+")
    url = f"https://www.bing.com/images/search?q={formatted_search_string}&count={num_images}"

    # send a request to the Bing search page and get the HTML content
    response = requests.get(url)
    html_content = response.text

    # parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # extract the image URLs from the BeautifulSoup object
    image_urls = []
    for img  in soup.find_all('img', class_="mimg"):
        try:
            image_urls.append(img['src'])
        except:
            #print(f"moving on to next image")
            break

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
search_string = "box on door steps"
num_images = 30
download_images(search_string, num_images)
"""