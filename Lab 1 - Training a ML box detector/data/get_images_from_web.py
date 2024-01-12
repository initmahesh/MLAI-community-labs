import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time

#Define path where to store images
path = 'sample_data'

#Chrome web driver
driver = webdriver.Chrome('chromedriver')

# Google images search URL
url = "https://www.google.com/search?q=cardboard+box&tbm=isch&ved=2ahUKEwjCvM-f-4L_AhVkk9gFHUFtAiQQ2-cCegQIABAA&oq=cardboard+box&gs_lcp=CgNpbWcQAzIKCAAQigUQsQMQQzIHCAAQigUQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOggIABCABBCxAzoHCCMQ6gIQJzoECCMQJ1AAWK8yYNYzaAJwAHgDgAGRBYgBwzGSAQswLjEuOC40LjEuNJgBAKABAaoBC2d3cy13aXotaW1nsAEKwAEB&sclient=img&ei=kT9oZIKwBuSm4t4PwdqJoAI&bih=746&biw=1536&rlz=1C1ONGR_enIN1012IN1012"
driver.get(url)

#Scrolls the page 4 times. Change to make it scroll more
for i in range(4):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #Paus of 5 seconds for images to render on screen.
    time.sleep(5)

#Gets the images from the page using html class name inside page's source
imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")
src = []

#Appends imgResults iteratively to store only the value of "src" from the image tag
for img in imgResults:
    src.append(img.get_attribute('src'))

#Saves images from list to defined path
def save_images_to_path():
    # Tune the range to get more images
    for i in range(200):    
        urllib.request.urlretrieve(str(src[i]),"sample_data/box{}.jpg".format(i))
    

#Make a directory to store images, skips if exist already
isExists = os.path.exists(path)
if(isExists):
    save_images_to_path()
else:
    os.makedirs(path)
    save_images_to_path()
