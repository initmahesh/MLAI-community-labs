# Scraping Google search results, is against Google's terms of service, and your IP may be temporarily or permanently blocked by Google if detected. Use this method at your own risk.

# When scraping Google Images search results directly from the HTML, the images you get are usually low-resolution thumbnail versions. 
# To get higher-resolution images, you can extract the image URLs from the JavaScript data embedded in the HTML instead of directly from the <img> elements. However, this doesn't work due to dynamic nature of Google's search results page


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

def get_image_urls(search_term, start):
    url = f"https://www.google.com/search?q={search_term}&tbm=isch&start={start}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    image_elements = soup.find_all("img")
    return [img["src"] for img in image_elements if "src" in img.attrs]

# Define the search term
search_term = "doorstep+boxes"

# Create output directory
output_dir = "doorstep_boxes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download and save images
image_count = 0
page_start = 0
while image_count < 200:
    image_urls = get_image_urls(search_term, page_start)

    if not image_urls:
        print("No more images found.")
        break

    for img_url in image_urls:
        if image_count >= 200:
            break
        download_image(img_url, output_dir, image_count)
        image_count += 1

    page_start += 20

print("Finished downloading images.")