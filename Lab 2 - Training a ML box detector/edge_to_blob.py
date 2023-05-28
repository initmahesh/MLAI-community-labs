import cv2
import os, time
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, PublicAccess, BlobType, generate_blob_sas, BlobSasPermissions
from azure.storage.queue import QueueServiceClient
from dotenv import load_dotenv
import os
import uuid
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import CustomVisionErrorException
from msrest.authentication import ApiKeyCredentials
from twilio.rest import Client

class VideoCaptureToBlob:
    def __init__(self, connection_string, source, time_delay, manual_mode, storage_account_key, account_name):
        self.account_name = account_name
        self.connection_string = connection_string
        self.source = source
        self.storage_account_key = storage_account_key
        self.time_delay = time_delay
        self.manual_mode = manual_mode
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        self.container_name = None 
        self.queue_service = None

    def create_storage(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.container_name = 'fromcamera' + timestr
        self.blob_service_client.create_container(self.container_name)
        self.container_client = self.blob_service_client.get_container_client(self.container_name)
        self.container_client.set_container_access_policy(signed_identifiers={}, public_access=PublicAccess.Container)
        self.queue_service = QueueServiceClient.from_connection_string(self.connection_string)
        self.queue_service.create_queue('fromcamera' + timestr)

    def capture_and_inference(self):
       if self.source is not None:
           if self.source == 'usb':
               cap = cv2.VideoCapture(0)
           else:
               cap = cv2.VideoCapture(self.source)
       else:
           print("Please set the valuse of SOURCE variable in .env file")
           return

       ret = True
       i = 0
       print('Created stream')
       if(self.manual_mode == 1):
           print('Press SPACE to capture or ESC to quit')
      
       while ret:
           ret, frame = cap.read()
           if(frame is None):
               print("Unable to capture frame from source :" + self.source)
               print("Please check correct SOURCE variable is set in .env file")
               break  

           if(self.manual_mode == 1):
               window_name = "Press SPACE to capture or ESC to quit"
               cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
               cv2.imshow(window_name, frame)
              
               k = cv2.waitKey(1)
               if k%256 == 27:
                   # ESC pressed
                   print("Escape hit, closing...")
                   cv2.destroyAllWindows()
                   break
                 
               elif k%256 == 32:
                   # SPACE pressed
                   i+=1 
                   self.upload_frame(frame, i)
           else:   
               ret, frame = cap.read()
               i+=1
               results = self.inference(frame)
               # Set the probability threshold (e.g., 0.8 for 80%)
               probability_threshold = 0.8

               # Display the results.
               # The bounding box values are normalized, which means they are in the range of 0 to 1 relative to the image dimensions.
               # To get the actual pixel coordinates, you can multiply these values by the width and height of the image, respectively.
               for prediction in results.predictions:
                if prediction.tag_name == 'Box':
                    if prediction.probability >= probability_threshold:
                       url = f'https://mlcohort.blob.core.windows.net/{self.container_name}/image{i}.jpg'

                       self.upload_frame(frame, i, '_without_overlay')

                       #Storing bounding_box coordinates as x an y axis
                       x = int(prediction.bounding_box.left * frame.shape[0])
                       y = int(prediction.bounding_box.top * frame.shape[1])

                       width = x + int(prediction.bounding_box.width * frame.shape[0])
                       height = y + int(prediction.bounding_box.height * frame.shape[1])

                       #Adding bounding_box to the frame
                       frame = cv2.rectangle(frame, (x, y), (width, height), (0, 0, 255), 2)
                       #Adding tag_name that we got from pridiction in the bounding_box
                       frame = cv2.putText(frame, prediction.tag_name, (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 1, cv2.LINE_AA, False)
                       
                       print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))
                       self.upload_frame(frame, i)
                       self.send_sms()
                       self.save_to_filesystem(frame)
                       time.sleep(self.time_delay)

                    else:
                       print("No object detected")
                       time.sleep(self.time_delay)
               else: 
                print('Something else was detected')
                
       cap.release()
       print('Released stream')


    def send_sms(self):
        blob_list = []

        for blob in self.container_client.list_blobs():
            if 'without' in blob.name:
                continue
            blob_list.append(blob)  


        sorted_list = sorted(blob_list, key=lambda e: e.creation_time, reverse=True)
        sas_i = generate_blob_sas(
                account_name= ACCOUNT_NAME,
                container_name= self.container_name,
                blob_name= sorted_list[0].name,
                account_key= STORAGE_ACCOUNT_KEY,
                permission= BlobSasPermissions(read=True),
                expiry= datetime.utcnow() + timedelta(hours=8760)
                )
        
        sas_url = 'https://' + ACCOUNT_NAME +'.blob.core.windows.net/' + self.container_name + '/' + sorted_list[0].name + '?' + sas_i

        message = client.messages.create(
                            body=f'A Box is detected at you door! In case you are out you can view the image here: {sas_url}',
                            from_= PHONE_NUMBER,
                            to='+917303879964'
                        )
       

    def upload_frame(self, frame, i, sufix=''):
        print("frame capture function returned :: " +  str(frame is not None) + " storing to container :: " + self.container_name)
        image_jpg = cv2.imencode('.jpg',frame)[1].tobytes()
        blob_name= 'image' + str(i) + sufix +'.jpg' if sufix else 'image' + str(i) +'.jpg'
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.upload_blob(image_jpg, blob_type=BlobType.BlockBlob)
        print("Total files stored :: " + str(i))


    def save_to_filesystem(self, frame):
        #Stores frame as jpg locally
        current_time = time.strftime("%Y-%m-%d %H-%M-%S")
        local_image_location = os.path.join(os.path.join(os.path.dirname(__file__), "test/"))
        cv2.imwrite(f"{local_image_location}/{current_time}.jpg", frame)


    def inference (self, frame):
       # Get the project by project_id
       try:
           iterations = trainer.get_iterations(PROJECT_ID)
           published_iteration = next(iteration for iteration in iterations if iteration.publish_name)
           publish_iteration_name = published_iteration.publish_name
       except StopIteration:
           print("No published iteration found. Please publish an iteration in the Custom Vision portal.")
           exit(1)

       image_jpg = cv2.imencode('.jpg',frame)[1].tobytes()
       results = predictor.detect_image(PROJECT_ID, publish_iteration_name, image_jpg)
       return results

if __name__ == "__main__":
    load_dotenv()
    CONNECTION_STRING = os.getenv('CONNECTION_STRING').strip()
    SOURCE = os.getenv('SOURCE')
    TIME_DELAY = int(os.getenv('TIME_DELAY'))
    MANUAL_MODE = int(os.getenv('MANUAL_MODE'))
    ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
    PREDICTION_KEY = os.environ['PREDICTION_KEY']
    TRAINING_KEY = os.environ['TRAINING_KEY']
    PROJECT_ID = os.environ['PROJECT_ID']
    ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
    ACCOUNT_NAME = os.environ['ACCOUNT_NAME']
    STORAGE_ACCOUNT_KEY = os.environ['STORAGE_ACCOUNT_KEY']

    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


    training_credentials = ApiKeyCredentials(in_headers={"Training-key": TRAINING_KEY})
    trainer = CustomVisionTrainingClient(ENDPOINT, training_credentials)

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    video_capture = VideoCaptureToBlob(CONNECTION_STRING, SOURCE, TIME_DELAY, MANUAL_MODE, STORAGE_ACCOUNT_KEY, ACCOUNT_NAME)
    video_capture.create_storage()
    video_capture.capture_and_inference()
