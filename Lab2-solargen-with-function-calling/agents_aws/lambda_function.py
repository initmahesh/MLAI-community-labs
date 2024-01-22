import json
import urllib3
import os

def create_lead(name, phone, address):
    # Airtable API URL
    url = "https://api.airtable.com/v0/appHi3S1HmZHJuGDq/Lead%20Gen"

    # Headers with Authorization and Content-Type
    headers = {
        "Authorization": os.getenv("AIRTABLE_API_KEY"),  # Takes Airtable API from environment
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
  geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={os.getenv('GOOGLE_API')}"
  # response = requests.get(geocoding_url)
  
  http = urllib3.PoolManager()

  # Make a POST request to Airtable API
  response = http.request(
        'GET',
        geocoding_url
    )
    
  if response.status == 200:
    response = response.data
    response = response.decode('utf-8')
    response = json.loads(response)
    print(response['results'][0]['geometry']['location'])
    location = response['results'][0]['geometry']['location']
    print(f"Coordinates for {address}: {location}")
    return location['lat'], location['lng']
  else:
    print(f"Error getting coordinates: {response.text}")
  # return '100.14.11.E.12','100.14.11.e.15'

def get_solar_data(lat, lng):
  solar_api_url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={lat}&location.longitude={lng}&requiredQuality=HIGH&key={os.getenv('GOOGLE_API')}"
  print(solar_api_url)
  # solar_api_url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude= 33.8342152&location.longitude= -118.1731399&requiredQuality=HIGH&key=AIzaSyAYqrCkY0rYn3nKCQS4fPtrpGjGWzqUCJ8"
  # response = requests.get(solar_api_url)
  
  http = urllib3.PoolManager()
  
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

def lambda_handler(event, context):
    responseCode = '200'
    apiPath = event['apiPath']
    parameters = {}
    print(event)
    if 'parameters' in event:
        parameters = event['parameters']
        
    if 'createLead' in apiPath:
        for item in parameters:
          if item['name'] == 'phoneNumber':
              phone_number = item['value']
          elif item['name'] == 'name':
              name = item['value']
          elif item['name'] == 'address':
              address = item['value']
        response = create_lead(name,phone_number,address)
    
    elif 'solarPanelCalculations' in apiPath:
        for item in parameters:
          if item['name'] == 'address':
              address = item['value']
          elif item['name'] == 'monthlyBills':
              monthly_bill = item['value']
      
        response = solar_panel_calculations(address, monthly_bill)
    
    else:
        raise Exception('Unrecognized API definition')
        
    responseBody={
        "application/json":{
            "body":str(response)
        }
    }
    
    action_response={
        'actionGroup':event['actionGroup'],
        'apiPath':event['apiPath'],
        'httpMethod':event['httpMethod'],
        'httpStatusCode':responseCode,
        'responseBody':responseBody
    }
    
    mock_api_response = {"response":action_response,'messageVersion':event['messageVersion']}
    return mock_api_response