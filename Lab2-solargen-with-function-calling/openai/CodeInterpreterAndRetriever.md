## Code Interpreter using OpenAI Assistants

### Using assistants for we can generate and run Python code in a sandboxed execution environment.
Below is an example for using the code interpreter.

Click on this link for the entire notebook: [Click](function_call_OpenAI.ipynb)

### Explaining the code:

Creating the message for assistants ```code_intructions``` and the instructions needed to run the thread ```code_run_ins

```python
code_instruction = '''you have the user_bill as integer and financial analysis which is a list of json objects that contains the monthlyBill and inside monthlyBill the units is stored, 
you need to write a code in python which calculates the absolute difference between the units and the user_bill that is stored in smallest_difference if it is smaller than the previous smallest difference 
and for the smallest difference the array object is stored in a variable called closest_match and the variable is returned.'''

code_run_instruction = '''Run the function with user_bill = <user_bill> and financial_analysis = <financial_analysis>. Display the code for the function and the entire array object stored in closest match'''
```

Creating an assistant object and calling the python assistant function that will create an assistant with code interpreter enabled

```python
code_obj = AssistantManager(os.getenv("Open_AI_key"))

code_obj.python_assistant(
    name = "Python Developer",
    instructions="You are a Senior Python developer and you job is to create ,run and display python codes and return the outputs",
    tools = [{'type':'code_interpreter'}]
)
```

Here we create a thread and add message to the thread that we created earlier as ```code_instruction```, then we run the thread with instructions that we created earlier ```code_run_instructions```

```python
time.sleep(5)
closest_match = ''
result =  [
    {"monthlyBill": {"units": 120}},
    {"monthlyBill": {"units": 160}},
    {"monthlyBill": {"units": 140}},
    # Add more entries as needed
]
user_bill = 100

code_obj.create_thread()

code_obj.add_message_to_thread(role="user",content=code_instruction)
code_obj.run_assistant(code_run_instruction.replace('<user_bill>',str(user_bill)).replace('<financial_analysis>',str(result)))
```

After this we retrieve the run status and check it, if the status is 'completed' then the message content is extracted and displayed.

```python
while True:
    time.sleep(5)
    run_status = code_obj.client.beta.threads.runs.retrieve(
        thread_id = code_obj.thread.id,
        run_id = code_obj.run.id
    )
    
    print(run_status.status)
    if run_status.status == 'completed':
        messages = code_obj.client.beta.threads.messages.list(thread_id = code_obj.thread.id)
        # for msg in messages.data:
        #   role = msg.role
        msg = messages.data[0]
        role = msg.role
        content = msg.content[0].text.value
        print(content)
        index = content.find('{')
        print(closest_match)
        break
    elif run_status.status=="failed":
        print(run_status.last_error)
    else:
        print("Waiting for the Assistant to process..")
```


## Here is the output for the message we created:

```
in_progress
Waiting for the Assistant to process..
in_progress
Waiting for the Assistant to process..
completed
The code for the function is as follows:


def find_closest_match(user_bill, financial_analysis):
    smallest_difference = float('inf')
    closest_match = None
    for entry in financial_analysis:
        units = entry.get('monthlyBill', {}).get('units', 0)
        difference = abs(units - user_bill)
        if difference < smallest_difference:
            smallest_difference = difference
            closest_match = entry
    return closest_match


When the function is called with `user_bill = 100` and `financial_analysis = [{'monthlyBill': {'units': 120}}, {'monthlyBill': {'units': 160}}, {'monthlyBill': {'units': 140}}]`, the closest match is found to be `{'monthlyBill': {'units': 120}}`.
```
### Retrieval using OpenAI assistants

In order to use retriever tool, it should be be described in the tools as such and passed while creating the assistant:

```python
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
                            "description": "Monthly Bills to be generated.For example: 700 for 700 USD monthly bill"
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
```
```python
api_key = os.getenv("Open_AI_key")
manager = AssistantManager(api_key)

manager.create_assistant(
    name = "LeadGen",
    instructions=assistant_instructions,
    tools = tools
)
```

The ```Knowledge.docx``` is uploaded to the OpenAI for retrieval in this way:
```python
self.file = self.client.files.create(file=open("knowledge.docx","rb"),purpose='assistants')
        self.assistant = self.client.beta.assistants.create(
            name = name,
            instructions = instructions,
            tools = tools,
            model = self.model,
            file_ids = [self.file.id]
        )
```

## Results of Knowledge retrieval
1. How is solar energy harnessed?


Solar energy is harnessed through the use of solar panels, also known as photovoltaic (PV) panels. These panels are made up of many solar cells, which are designed to capture the sun's energy and convert it into electricity. When sunlight hits the solar panels, the semiconducting materials within the panels create an electric field that allows the flow of electricity. This electricity is then collected and can be used to power homes, businesses, and other electrical devices. Would you like to know more about solar energy or do you have any other specific questions?



2. How can you understand the solar potential of a particular place?


The solar potential of a particular place can be understood by analyzing factors such as the location's sun exposure, weather conditions, and shading. Additionally, the solar potential can be estimated by considering the electricity consumption of the place and the suitability for installing solar panels. Advanced tools and calculations can be used to determine the solar potential of a specific location.
If you’d like to calculate the solar potential of a particular place, I can help with that. Just provide me with the address and the approximate monthly electricity bill for the place in question.



3. What is the cheapest solar product?



The cheapest solar product can vary based on the specific need or application. However, some of the more affordable solar products include solar garden lights, solar phone chargers, and small solar panels for individual use. For larger-scale applications, cost-effectiveness is determined by factors such as the energy output, efficiency, and longevity of the solar products. If you have a specific solar product in mind or a particular use case, feel free to let me know!



4. How are solar panels connected in string inverters?



In string inverters, solar panels are typically connected in series to form a string. Multiple strings of solar panels are then connected to the string inverter. The series connection of solar panels in a string allows for higher DC voltage input to the inverter, which then converts the DC power to AC power for use in homes or businesses. However, it's important to note that shading or issues with one panel in a string can affect the performance of the entire string. This is why careful design and consideration of shading and panel orientation is vital when using string inverters.
If you need more detailed information or have further questions about solar panel connections or inverters, feel free to ask!



5. How do you calculate solar potential?



To calculate the solar potential of a specific location, I would need the address of the location and the approximate monthly electricity bill. With this information, I can perform a solar panel calculations to determine the solar potential and provide you with a detailed financial analysis based on the specific location and electricity usage.
If you have the address and the monthly electricity bill for a particular location, please provide that information so that we can proceed with the solar potential calculation.

