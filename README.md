# MLAI-community-labs
Labs that explain complex ML/AI ideas simply with code.

# Training a ML box detector
Using Azure custom vision and cognitive service, we are training a model to detect boxes, once a box is detected it will 
notify the user along with an image showing where the box is. 

# Requirements
- [Azure computer vision](https://github.com/Azure/azure-sdk-for-python)
- [Azure custom vision](https://github.com/Azure/azure-sdk-for-python)
- [Azure storage](https://github.com/Azure/azure-sdk-for-python)
- [Beautiful soup](https://pypi.org/project/beautifulsoup4/)
- [Msrest](https://github.com/Azure/msrest-for-python)
- [OpenCV](https://github.com/opencv/opencv-python)
- [Twilio](https://github.com/twilio/twilio-python/)

# In a Nutshell
- Add all the required variables from `edge_to_blob.py` in a .env file
- The source can be direct video stream from a camera(USB), or from a .mp4 file.
- Time delay sets the time threshold to capture frames from the video.
- You can choose from two modes, manual(1) or auto(0).
- Finally, `py edge_to_blob.py`