# Function calling with OpenAI

Assistants are useful in ```code interpretation```,```retrieval``` and ```function calling```. In this readme, there is a description for the notebook which shows the creation of assistants and calling them for function calling.

## Prerequisites

### Resources you need to reproduce the results:

1. Python runtime (https://www.python.org/downloads/)
2. Git (https://www.git-scm.com/downloads)
3. Code Interpreter(for example: Vscode) (https://code.visualstudio.com/download)
4. Github account (https://github.com/)

### Refer to this readme, for creating the Google API.
[README](Lab2-OpenAIsolargenwithfunctioncalling/googleapi.md)

Now that google API is set and ready to use. Finally we will setup the Airtable for CRM. Let's set it up.

### Refer to this readme, for creating the Airtable API

[README](Lab2-OpenAIsolargenwithfunctioncalling/airtableapi.md)

# If you want to understand the code refer to the section as 'Now lets get into the code'
## Here we will explain how to run the frontend and backend locally as well as deploying them.

### For frontend and backend on the local server:
1. Clone the repository and navigate to './research/experiments/OpenAI_function_Call/frontend/'
2. Use a code editor such as VS code, open up a new terminal and run ```npm i``` or ```npm install```, this will download all the required node dependencies.
3. Now run ```npm start```, and the server will be up and running.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/48d9c5bd-4aa8-4a60-8199-a6bf67ee2860)
   
4. Now open a terminal in the root folder and run ```python manage.py runserver```, the backend will have started now.
5. Now go to the wepage that you hosted in step 3, and click on the message icon.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/42dbec75-06c9-452e-a301-8187851e45c8)
6. A message box opens up and you can chat with the Assistant.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/348420a2-8599-4422-8e92-ea7c53daeda4)
7. The Assistant is meant to only calculate the solar potential and take information from the user to create leads for contacting in future.

The prompt has been made in such a way that, the assistant will ask for any missing information before executing any function.

### For deploying the frontend and backend and using the chat bot, follow the steps below.

1. Visit https://render.com/ and create an account on it using your Github account. The github account should have the repository containing the backend code.
2. Click on New and select web services.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/730080bb-a0f1-49ed-9b0f-916562f34468)
3. Select Build and deploy from github repository.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/ba30b575-0bdf-417d-83d4-45370bf28b6b)
4. Your repository should show up here
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/071abf21-7917-4419-815c-204b9897dd80)
5. Click on Connect on the repository which stores the code for backend.
6. Give the name of the web service.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/609c46b8-3f0d-4e9b-92b7-3c9ceba47927)
7. Select the branch that stores the backend code.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/fb8f925e-1649-4409-90ab-5772993b9ffb)
8. Select the runtime as python 3
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/2ea736a7-f7f6-424d-b484-e13dd0041b58)
9. Select create web service.
10. Go Dashboard->Your deployment->settings, scroll down to Start Command.
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/1756b599-9821-4dc1-9368-70d9db31caf8)


    and set it as ```python manage.py runserver 0.0.0.0:8000```
11. Now you are all set up. Everytime there is commit on the branch that you selected, the deployment will detect it and update the deployment.
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/55380a0d-aaea-446d-9615-a3f4dc03c07c)

    The deployment should look like this and the status should show ```Deployed```. You should find you endpoint here

    
    ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/8845c213-0296-4340-89f3-6ce0696c6421)


Now that the backend has been deployed, let's turn to frontend deployment on render.

1. Visit https://vercel.com/, and create an account on it using your email (you can use your Github account too).
2. Navigate to './research/experiments/OpenAI_function_Call/frontend/'.


   Go to App.js in './research/experiments/OpenAI_function_Call/frontend/src' and replace this line with your backend endpoint

   
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/77e56ad4-4866-455b-9822-b2ae9e4f5d29)  

5. Use a code editor such as VS code, open up a new terminal and run ```npm i``` or ```npm install```, this will download all the required node dependencies.

6. Now we need to install vercel globally ```npm i -g vercel```, this will install vercel.
7. Now use the command ```vercel``` in the same terminal. This will load up the CLI for vercel. Type 'y' for set up and deploy (Make sure that the directory is correct and contains the frontend files)
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/f4ba964f-bb16-44d7-83ac-e37ba9821cae)
8. Select the project that you want to deploy the frontend is.
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/31eb4350-3afa-4404-8e86-0ca8af509aac)

   
   Say 'n' for linking to an existing project

   
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/d5ff8f89-9bed-48e4-92c4-207e640941d4)

   
   If you want to change the name of the project specify it or it will take the directory name as the default project name.

   
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/f200243d-3f6b-4e53-8601-8b11a9bb93bb)


   Select the directory in which the code is located


   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/291f572b-6d49-48aa-a541-b17c91915f6a)


   Vercel CLI with auto detect the project setting and you can give 'n' to this


   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/8ba7f784-ebeb-4ce2-a822-adfd69151dab)

   
   The frontend has now been deployed and you can click on the production link to visit the website.
   
   ![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/72266e34-2970-4dd4-947e-859673f04267)


#### One last thing:

Add your frontend endpoint and backend endpoint in the settings.py file of backend and push to the repository.


![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/b0f680a6-8fe0-4621-8f54-df3896f18fda)



## Now lets get into the code.
Firstly we define the functions create_lead() and solar_potential_calculations()
```python
import json
import urllib3
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API = os.getenv('GOOGLE_API')
AIRTABLE_API = os.getenv('AIRTABLE_API')


def create_lead(name, phone, address):
    # Airtable API URL
    url = "https://api.airtable.com/v0/appHi3S1HmZHJuGDq/Lead%20Gen"

    # Headers with Authorization and Content-Type
    headers = {
        "Authorization": AIRTABLE_API,  # Takes Airtable API from environment
        "Content-Type": "application/json"
    }

    # Data to be sent in the request
    data = {
        "records": [{
            "fields": {
                "Name": name,
                "Phone": phone,
                "Address": address,
                "Status": "Arrived"
            }
        }]
    }

    # Create a PoolManager for HTTP requests
    http = urllib3.PoolManager()

    # Encode data to bytes
    encoded_data = json.dumps(data).encode('utf-8')

    # Make a POST request to Airtable API
    response = http.request(
        'POST',
        url,
        body=encoded_data,
        headers=headers
    )

    # Check the response status
    if response.status == 200:
        print("Lead created successfully.")
        return response
    else:
        print(f"Failed to create lead: {response.data}")

# Example usage:
# create_lead("John Doe", "1234567890", "123 Main St")
def get_coordinates(address):
  geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_API}"
  # response = requests.get(geocoding_url)

  timeout = urllib3.Timeout(connect=5.0, read=15.0)
  http = urllib3.PoolManager(timeout = timeout)

  # Make a POST request to Airtable API
  response = http.request(
        'GET',
        geocoding_url
    )

  if response.status == 200:
    response = response.data
    response = response.decode('utf-8')
    response = json.loads(response)
    print(response)
    print(response['results'][0]['geometry']['location'])
    location = response['results'][0]['geometry']['location']
    print(f"Coordinates for {address}: {location}")
    return location['lat'], location['lng']
  else:
    print(f"Error getting coordinates: {response.text}")
  # return '100.14.11.E.12','100.14.11.e.15'

def get_solar_data(lat, lng):
  solar_api_url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={lat}&location.longitude={lng}&requiredQuality=HIGH&key={GOOGLE_API}"
  print(solar_api_url)
  # solar_api_url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude= 33.8342152&location.longitude= -118.1731399&requiredQuality=HIGH&key=AIzaSyAYqrCkY0rYn3nKCQS4fPtrpGjGWzqUCJ8"
  # response = requests.get(solar_api_url)

  timeout = urllib3.Timeout(connect=5.0, read=15.0)
  http = urllib3.PoolManager(timeout=timeout)

  response = http.request(
        'GET',
        solar_api_url
    )

  print(response)
  if response.status == 200:
    response = response.data
    response = response.decode('utf-8')
    print("Solar data retrieved successfully.")
    response = json.loads(response)
    return response
  else:
    print(f"Error getting solar data: {response.text}")
  # return{
  #   "solarPotential":{
  #     "financialAnalyses":
  #       [{
  #         "monthlyBill":{
  #             "units":20
  #         }
  #       },
  #       {
  #         "monthlyBill":{
  #             "units":30
  #         }
  #       },
  #       {
  #         "monthlyBill":{
  #             "units":10
  #         }
  #       }]
  #   }
  # }

def extract_financial_analyses(solar_data):
  try:
    return solar_data.get('solarPotential', {}).get('financialAnalyses', [])
  except KeyError as e:
    print(f"Data extraction error: {e}")

def get_financial_data_for_address(address):
  lat, lng = get_coordinates(address)
  if not lat or not lng:
    return {"error": "Could not get coordinates for the address provided."}
  return extract_financial_analyses(get_solar_data(lat, lng))

def find_closest_financial_analysis(user_bill, financial_analyses):
  closest_match = None
  smallest_difference = float('inf')
  # for analysis in financial_analyses:
  #   bill_amount = int(analysis.get('monthlyBill', {}).get('units', 0))
  #   difference = abs(bill_amount - user_bill)
  #   if difference < smallest_difference:
  #     smallest_difference = difference
  #     closest_match = analysis
  # return closest_match
  for analysis in financial_analyses:
      # Accessing the nested dictionary
      monthly_bill_data = analysis.get('monthlyBill', {})

      # Extracting units
      bill_amount = int(monthly_bill_data.get('units', 0))
      difference = abs(bill_amount - user_bill)

      if difference < smallest_difference:
        smallest_difference = difference
        closest_match = analysis
  return closest_match

def simplify_financial_data(data):
  try:

    # data_str = json.dumps(data, indent=2)

    # # Getting formatter prompt from "prompts.py" file
    # system_prompt = formatter_prompt

    # # Replace 'client' with your actual OpenAI client initialization.
    # completion = client.chat.completions.create(
    #     model="gpt-4-1106-preview",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content":
    #             system_prompt  # Getting prompt from "prompts.py" file
    #         },
    #         {
    #             "role":
    #             "user",
    #             "content":
    #             f"Here is some data, parse and format it exactly as shown in the example: {data_str}"
    #         }
    #     ],
    #     temperature=0)

    # simplified_data = json.loads(completion.choices[0].message.content)
    # print("Simplified Data:", simplified_data)
    # return simplified_data
    return data

  except Exception as e:
    print("Error simplifying data:", e)
    return None

def solar_panel_calculations(address, monthly_bill):

  financial_analyses = get_financial_data_for_address(address)
  if "error" in financial_analyses:
    print(financial_analyses["error"])
    return financial_analyses
  closest_financial_analysis = find_closest_financial_analysis(
      int(monthly_bill), financial_analyses)
  print(closest_financial_analysis)
  if closest_financial_analysis:
    return simplify_financial_data(closest_financial_analysis)
  else:
    print("No suitable financial analysis found.")
    return {
        "error": "No suitable financial analysis found for the given bill."
    }
```
Then we go on to describe the tools/functions.
```python
tools = [
        {
            "type": "function",
            "function": {
                "name": "solar_panel_calculations",
                "description": "Calculate solar potential based on a given address and monthly electricity bill in USD. Returns financial analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "address": {
                            "type": "string",
                            "description": "Address for calculating solar potential.",
                        },
                        "monthly_bill":{
                            "type":"string",
                            "description": "Monthly Bills to be generated."
                        }
                    },
                    "required": ["address","monthly_bill"],
                },
            }
        },
        {
        "type":"function", 
        "function":{
                "name": "create_lead",
                "description": "Calculate solar potential based on a given address and monthly electricity bill in USD. Returns financial analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name":{
                              "type":"string",
                              "description":"Name of the lead."
                          },
                        "phone":{
                              "type":"string",
                              "description":"Phone number of the lead."
                          },
                        "address":{
                              "type":"string",
                              "description":"Address of the lead."
                        }
                    },
                    "required": ["name","phone","address"],
                },
            }
        }
    ]
```
Then we create a class called AssistantManager containing all the functions related to Assistant creation, running and executing the function name that has been returned.

This function creates the assistant in the OpenAI Assistants(This will also return the assistant id which will be used later for running the thread)
```python
def create_assistant(self,name, instructions, tools):
    self.assistant = self.client.beta.assistants.create(
        name = name,
        instructions = instructions,
        tools = tools,
        model = self.model
    )
```

The following 2 functions creates thread and adds message to the thread for generating the response
```python
def create_thread(self):
    self.thread = self.client.beta.threads.create()

  def add_message_to_thread(self,role,content):
    self.client.beta.threads.messages.create(
      thread_id = self.thread.id,
      role = role,
      content = content
    )
```

The run_assistant function is used for running the assistant with some extra instructions passed to it.
```python
def run_assistant(self,instructions):
    self.run = self.client.beta.threads.runs.create(
      thread_id = self.thread.id,
      assistant_id=self.assistant.id,
      instructions = instructions
    )
```

The wait_for_completion() and call_required_function() works together for generating the function name and executing it, after which the output from the tool is submitted back to the assistants for getting a proper response.
```python
def wait_for_completion(self):
    while True:
      time.sleep(5)
      run_status = self.client.beta.threads.runs.retrieve(
        thread_id = self.thread.id,
        run_id = self.run.id
      )
      print(run_status.model_dump_json(indent=4))

      if run_status.status == 'completed':
        self.process_messages()
        break
      elif run_status.status == 'requires_action':
        print("Function Calling ...")
        self.call_required_functions(run_status.required_action.submit_tool_outputs.model_dump())
      else:
        print("Waiting for the Assistant to process..") 
  
  def call_required_functions(self, required_actions):
    tool_output = []

    for action in required_actions["tool_calls"]:
      func_name = action['function']['name']
      arguments = json.loads(action['function']['arguments'])
    
      func_name = eval(func_name)
      output = func_name(**arguments)
      tool_output.append(
        {
          "tool_call_id":action['id'],
          "output": str(output)
        }
      )
    
    print(tool_output)
    print("Submitting outputs back to the Assistants...")
    self.client.beta.threads.runs.submit_tool_outputs(
      thread_id = self.thread.id,
      run_id = self.run.id,
      tool_outputs=tool_output
    )
```

Now we create the assistant->create thread->add message to the thread->run the assistant->wait for completion
```python
manager.create_assistant(
    name = "LeadGen",
    instructions="Extract name, phone number and address for lead generation. Or extract address and monthly bill for calculating solar potential.",
    tools = tools
)

manager.create_thread()
# manager.add_message_to_thread(role="user",content="Calculate solar potential for 9813 Sherborne Ave, Bakersfield, CA 93311, USA with monthly bill as 300 USD")
manager.add_message_to_thread(role="user",content="Create a lead for Mahesh Yadav, California, 33452213998")

manager.run_assistant("You are a solar panel financial advisor, your job is to extract address and monthly bills for calling functions to calculate solar potential. You also are a solar panel lead generation employee, your job is to extract personal details like name, phone number and address for returning as response for calling functions to generate leads. Strictly respond to the question for calling the function that is required to answer.Invoke only one function")
manager.wait_for_completion()
```

We can see that the output is generated as per the question/message:

Message
```Create a lead for Mahesh Yadav, California, 33452213998```
```python
<built-in method capitalize of str object at 0x000001D0363AAFF0>:Lead has been created for Mahesh Yadav with the phone number 33452213998 and the address in California.
```
![image](https://github.com/chatcontract/django-ml-backend/assets/72710483/2e7b6e43-df95-4675-85fd-90199aed096a)

Message
```Calculate solar potential for 9813 Sherborne Ave, Bakersfield, CA 93311, USA with monthly bill as 300 USD```
```python
<built-in method capitalize of str object at 0x000001D0363C4DF0>:The solar potential for the address 9813 Sherborne Ave, Bakersfield, CA 93311, USA with a monthly bill of 300 USD is as follows:
- Initial AC kWh per year: 13199.678
- Net metering allowed: Yes
- Solar percentage: 99.15%
- Percentage exported to grid: 66.36%
- Federal incentive: $6,837
- Cost of electricity without solar over lifetime: $89,983
- Estimated payback period for cash purchase: 5.25 years
- Financially viable for leased, cash purchase, and financed purchase options.

If you would like more details or assistance with solar panel installation, feel free to reach out!
```
