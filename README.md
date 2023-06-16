# MLAI-community-labs
Labs that explain complex ML/AI ideas simply with code.

# Training a ML box detector
Using Azure custom vision and cognitive service, we are training a model to detect boxes, once a box is detected it will 
notify the user along with an image showing where the box is. 

# Requirements
- [Azure computer vision](https://github.com/Azure/azure-sdk-for-python)
- [Azure custom vision](https://github.com/Azure/azure-sdk-for-python)
- [Azure storage](https://github.com/Azure/azure-sdk-for-python)
- [Msrest](https://github.com/Azure/msrest-for-python)
- [OpenCV](https://github.com/opencv/opencv-python)
- [Twilio](https://github.com/twilio/twilio-python/)
- [Selenium](https://pypi.org/project/selenium/)

# In a Nutshell
- Install all the required modules from requirements.txt `pip install -r requirements.txt`
- Add all the following required variables in a .env file
```env
CONNECTION_STRING = Storage connection string from Azure storage
SOURCE = 'usb' or path to any .mp4 file
TIME_DELAY = Specifies frame capture interval in seconds
MANUAL_MODE = Set 0 for auto and 1 for manual mode
PREDICTION_KEY = Azure cognitive service key
PROJECT_ID = Custom vision project id
TWILIO_ACCOUNT_SID = Account SID from twilio
TWILIO_AUTH_TOKEN = Auth Toekn from twilio
TWILIO_PHONE_NUMBER = Twilio phone number
ACCOUNT_NAME = Azure account name
BLOB_ACCOUNT_KEY = Storage account key
ENDPOINT_CUSTOM_VISION = Azure custom vision endpoint
SERPAPI_API_KEY = Serpapi API key for scraping tool.
```
- The source can be direct video stream from a camera(USB), or from a .mp4 file or RTSP stream .
- Time delay sets the time threshold to capture frames from the video.
- You can choose from two modes, manual(1) or auto(0).
- Finally, `py edge_to_blob.py`

# Using the scraper 
If you wish to train the model with your own data you can use the provided scraper which uses silenium to scrape images from the internet. Refer this readme to know how to set up and run the provided scraper. `silenium readme link here`

# Training your own ML model
You can also train the Model using Azure custom vision and cognitive service. Follow these steps to train the ML model.

Follow this how to guide here: 

# Quick tutorial
https://github.com/initmahesh/MLAI-community-labs/assets/62789637/8a5d3306-94c5-42d9-9b7e-40c9eea407c6

