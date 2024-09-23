## This project demonstrates how to use Mediapipe to compress a Gemma model into a TensorFlow Lite model.

## Requirements

- Jupyter Notebook
- Mediapipe
- TensorFlow
- Hugging Face token (for downloading the Gemma model)

Steps
1. Download the Gemma Model
To download the Gemma model, you need a Hugging Face token. You can obtain one by creating an account on the Hugging Face website.


You can download the tflite model directly using the following link:

[Download Gemma Model](https://drive.google.com/file/d/1-1SgjPC2txY57YPGi3Sf633H98wO9Hjd/view?usp=drive_link)


2. Compress the Model
Open the provided Jupyter Notebook to use Mediapipe for compressing the Gemma model into a TensorFlow Lite model.

3. Update the Model Name
After downloading the model, you will need to replace the model name in the provider index.js script. Make sure to set it to the name of the model you downloaded.

4. Start the Python Server
Run the following command in your terminal to start the Python server:

```bash
python3 -m http.server 8000
````

5. Access the Model
Navigate to http://localhost:8000 in your web browser to access the server.