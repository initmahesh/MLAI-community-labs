import os
import requests
from bs4 import BeautifulSoup

def download_image(url, output_dir, count):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        file_name = f"{output_dir}/image_{count:03d}.jpg"

        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded image {count + 1}: {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image {count + 1}: {e}")

# Define the search term
search_term = "doorstep+boxes"

# Get the Google Images search results page
url = f"https://www.google.com/search?q={search_term}&tbm=isch"

# Make a request to the Google Images search results page
response = requests.get(url)

# Parse the response as HTML
soup = BeautifulSoup(response.content, "html.parser")

# Find all of the image elements on the page
image_elements = soup.find_all("img")

# Get the image URLs
image_urls = [image_element["src"] for image_element in image_elements if "src" in image_element.attrs]

# Create output directory
output_dir = "doorstep_boxes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download and save images
for count, img_url in enumerate(image_urls[:200]):
    download_image(img_url, output_dir, count)