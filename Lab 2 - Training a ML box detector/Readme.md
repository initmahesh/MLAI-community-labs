# Using the provided scraping tool. 
`get_hd_images_serpapi.py`

To get high quality images from google we are using a third pary service `Serpapi`. 

# Setting up and running the scraper
To get started with the scraper we first need to get an API key from `serpapi`, we need this so that our API request can be authenticated.

Follow these steps to generate your own serpapi API key:

- Step 1: Go to `https://serpapi.com/`.

  ![1](https://github.com/initmahesh/MLAI-community-labs/assets/62789637/9cc06cfd-51b6-4a0b-9819-50be94117e58)

- Step 2: Register yourself on the platform.
  
  ![2](https://github.com/initmahesh/MLAI-community-labs/assets/62789637/2e684c89-cb54-4dc6-8281-a4bbf8466ba2)

- Step 3: You should see an API key on the dashboard.
  
  ![3](https://github.com/initmahesh/MLAI-community-labs/assets/62789637/a859fb0f-4e3f-4204-9ef1-b842063012d8)

- Step 4: Copy that key that's what we need.
  
  ![4](https://github.com/initmahesh/MLAI-community-labs/assets/62789637/67a4ea46-57c7-4fd4-85cf-eb1ee567e650)

- Step 5: Add the key you just copied to the .env file.
  
  ![5](https://github.com/initmahesh/MLAI-community-labs/assets/62789637/ee95f45f-41d0-44b4-bba2-fefc8d04ac6f)

- Step 6: If you haven't installed the project requirements install them from the requirements.txt file or by simply running `$ pip install -r requirements.txt`.

- Step 7: Inside `get_hd_images_serpapi.py` add your search query for the images you want.
  
  ![7](https://github.com/initmahesh/MLAI-community-labs/assets/62789637/412bcebe-b0be-4dac-87d4-564a22f83a85)

- Step 8: Now run the code and wait till all the processing is done. Run by typing `py get_hd_images_serpapi.py` in your terminal. 
  
  ![8](https://github.com/initmahesh/MLAI-community-labs/assets/62789637/e8580058-0de4-4fa6-ae2b-0b44f42c5272)
