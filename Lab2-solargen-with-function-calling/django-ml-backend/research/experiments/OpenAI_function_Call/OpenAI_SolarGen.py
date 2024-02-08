import json
import urllib3
import os
from dotenv import load_dotenv
from .prompts import formatter_prompt,assistant_instructions
from openai import OpenAI
import time

load_dotenv()

GOOGLE_API = os.getenv('GOOGLE_API')
AIRTABLE_API = os.getenv('AIRTABLE_API')
AIRTABLE_URL = os.getenv('AIRTABLE_URL')

class AssistantManager:
  def __init__(self,api_key:str,model:str="gpt-3.5-turbo-1106"):
    self.client = OpenAI(api_key=api_key)
    self.model = model
    self.assistant = None
    self.thread = None
    self.run = None
    self.file = None
    self.message = None

  def python_assistant(self,name, instructions, tools):
        self.assistant = self.client.beta.assistants.create(
            name = name,
            instructions = instructions,
            tools = tools,
            model = self.model
        )

  def create_assistant(self,name, instructions, tools,id):
        self.file = self.client.files.create(file=open(r"research/experiments/OpenAI_function_Call/knowledge.docx","rb"),purpose='assistants')
        assistant_file_path = './research/experiments/OpenAI_function_Call/assistant.json'
        if os.path.exists(assistant_file_path):
          with open(assistant_file_path, 'r') as file:
            assistant_data = json.load(file)
            if f'{id}' in assistant_data:
              assistant_id = assistant_data[f'{id}']['assistant_id']
              self.assistant = self.client.beta.assistants.retrieve(assistant_id)
              file.close()
            else:
               self.assistant = self.client.beta.assistants.create(
                name = name,
                instructions = instructions,
                tools = tools,
                model = self.model,
                file_ids = [self.file.id]
                )
               assistant_data[f'{id}'] = {'assistant_id': self.assistant.id}
               with open(assistant_file_path, 'w') as file:
                json.dump(assistant_data, file)
                file.close()
               
        else:
            self.assistant = self.client.beta.assistants.create(
                name = name,
                instructions = instructions,
                tools = tools,
                model = self.model,
                file_ids = [self.file.id]
            )
            with open(assistant_file_path, 'w') as file:
              json.dump({f'{id}':{'assistant_id': self.assistant.id}}, file)
              print("Created a new assistant and saved the ID.")
              file.close()

  def create_thread(self,id):
      thread_file_path = './research/experiments/OpenAI_function_Call/assistant_thread.json'
      if os.path.exists(thread_file_path):
        with open(thread_file_path, 'r') as file:
          thread_data = json.load(file)
          if f'{id}' in thread_data:
            thread_id = thread_data[f'{id}']['thread_id']
            self.thread = self.client.beta.threads.retrieve(thread_id = thread_id)
            file.close()
          else:
             self.thread = self.client.beta.threads.create()
             thread_data[f'{id}'] = {'thread_id': self.thread.id}
             with open(thread_file_path, 'w') as file:
              json.dump(thread_data, file)
              file.close()
      else:
        self.thread = self.client.beta.threads.create()
        with open(thread_file_path, 'w') as file:
              json.dump({f'{id}':{'thread_id': self.thread.id}}, file)
              print("Created a new thread and saved the ID.")
              file.close()

  def add_message_to_thread(self,role,content):
    self.message = self.client.beta.threads.messages.create(
      thread_id = self.thread.id,
      role = role,
      content = content
    )

  def run_assistant(self,instructions):
    self.run = self.client.beta.threads.runs.create(
      thread_id = self.thread.id,
      assistant_id=self.assistant.id,
      instructions = instructions
    )

  def process_messages(self):
    messages = self.client.beta.threads.messages.list(thread_id = self.thread.id)

    msg = messages.data[0]
    role = msg.role
    content = msg.content[0].text.value
    print(f"{role.capitalize}:{content}")
    return content

  def wait_for_completion(self):
    while True:
      time.sleep(5)
      run_status = self.client.beta.threads.runs.retrieve(
        thread_id = self.thread.id,
        run_id = self.run.id
      )
      
      print(run_status.status)
      if run_status.status == 'completed':
        return(self.process_messages())
        break
      elif run_status.status == 'requires_action':
        print("Function Calling ...")
        self.call_required_functions(run_status.required_action.submit_tool_outputs.model_dump())
      elif run_status.status=="failed":
        print(run_status.last_error)
        return ("The assistant got rate limited, try again after some time or refresh the page and try again")
        break
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
    
    print("Submitting outputs back to the Assistants...")
    self.client.beta.threads.runs.submit_tool_outputs(
      thread_id = self.thread.id,
      run_id = self.run.id,
      tool_outputs=tool_output
    )



def create_lead(name, phone, address):
    # Airtable API URL
    url = AIRTABLE_URL

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
    location = response['results'][0]['geometry']['location']
    print(f"Coordinates for {address}: {location}")
    return location['lat'], location['lng']
  else:
    print(f"Error getting coordinates: {response.text}")
  # return '100.14.11.E.12','100.14.11.e.15'

def get_solar_data(lat, lng):
  # The solar data for a given latitude and longitude is retrieved using this URL
  solar_api_url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={lat}&location.longitude={lng}&requiredQuality=HIGH&key={GOOGLE_API}"

  timeout = urllib3.Timeout(connect=5.0, read=15.0)
  http = urllib3.PoolManager(timeout=timeout)

  response = http.request(
        'GET',
        solar_api_url
    )
  
  if response.status == 200:
    response = response.data
    response = response.decode('utf-8')
    print("Solar data retrieved successfully.")
    response = json.loads(response)
    return response
  else:
    print(f"Error getting solar data: {response.text}")

def extract_financial_analyses(solar_data):
  try:
    # Getting the financial analyses from the solar data.
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

    data_str = json.dumps(data, indent=2)

    # Getting formatter prompt from "prompts.py" file
    system_prompt = formatter_prompt
    api_key = os.getenv("Open_AI_key")

    client = OpenAI(api_key= api_key)
    # Replace 'client' with your actual OpenAI client initialization.
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content":
                system_prompt  # Getting prompt from "prompts.py" file
            },
            {
                "role":
                "user",
                "content":
                f"Here is some data, parse and format it exactly as shown in the example: {data_str}"
            }
        ],
        temperature=0)

    simplified_data = json.loads(completion.choices[0].message.content)
    return simplified_data

  except Exception as e:
    print("Error simplifying data:", e)
    return None

def solar_panel_calculations(address, monthly_bill):

  financial_analyses = get_financial_data_for_address(address)
  if "error" in financial_analyses:
    print(financial_analyses["error"])
    return financial_analyses
  monthly_bill = [i for i in str(monthly_bill) if i.isdigit() or i == '.']

  monthly_bill = float(''.join(monthly_bill))
  closest_financial_analysis = find_closest_financial_analysis(
      int(monthly_bill), financial_analyses)
  if closest_financial_analysis:
    return simplify_financial_data(closest_financial_analysis)
  else:
    print("No suitable financial analysis found.")
    return {
        "error": "No suitable financial analysis found for the given bill."
    }
  
tools = [{"type":"retrieval"},
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
                            "type":"integer",
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
                "description": "Create a lead using the name , phone number and address.",
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


instruction1 = '''
Greet the User if they say 'Hi' or 'Hey' or something similar.
If the user asks what the assistant is capable of, the assistant should be short and precise with their response and talk about the assistant's functionalities.

If the user wants to calculate solar potential, and provides the address and the monthly bill, the assistant should take this information to calulate solar potential. 
If the user does not provide address or monthly bill, the assistant should request the user for it. The assistant should not call the calculate solar potential function unless it has all the properties it needs.
If the address and monthly bill is provided, go ahead and call the function solar_panel_calculations and return the detailed calculations to the user along with a question in the end as "Please provide your name, phone number and address for contacting you".

If the user provides the name, phone number and address for creating lead, the assistant should take this information to create lead.
If the user does not give name or phone number or address, the assistant should request the user to provide it. The assistant should not call the create lead function unless it has all the properties it needs.
Once it has all the information, it can go ahead and call the function create_lead. If the lead is created successfully, the assistant should say "Thank you for providing your information. Someone from the team will get in touch with you to discuss further details."

Assistant should strictly follow this:
Do not ask for name, address, phone number before calculating solar potential
The assistant is not capable of making up random values for any missing information. The assistant should always have all the information it needs before calling the function. The assistant should remember the context of a question.
Extract the monthly bill without currency, for example: if user gives monthly bill as "300 USD" the assistant should extract "300" or "$300" should be extracted as "300"
Assistant should also follow this as side note:
If no suitable financial analysis is found, then assistant should say "I apologize, but it seems that no suitable financial analysis was found for the given monthly bill.This could maybe happen because of missing solar data on your location or the monthly bill is not suitable."
'''

instruction2 = '''
The assistant is a solar panel financial advisor, its job is to extract address and monthly bills for calling functions to calculate solar potential. 
The assistant can also ask for name, phone number and address for lead generation after the solar potential is generated.
'''

def gen_answer(query,id):

    api_key = os.getenv("Open_AI_key")
    manager = AssistantManager(api_key)

    manager.create_assistant(
    name = "LeadGen",
    instructions=assistant_instructions,
    tools = tools,
    id = id
    )
    time.sleep(3)
    manager.create_thread(id)
    # manager.add_message_to_thread(role="user",content="Calculate solar potential for 9813 Sherborne Ave, Bakersfield, CA 93311, USA with monthly bill as 300 USD")
    manager.add_message_to_thread(role="user",content=query)

    manager.run_assistant(instruction1)
    try:
      return(manager.wait_for_completion())
    except Exception as e:
      print("Error: "+str(e))
      return ("The assistant got stuck, please refresh the page and try again")