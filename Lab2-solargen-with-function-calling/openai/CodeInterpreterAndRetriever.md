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

```python
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
```

When the function is called with `user_bill = 100` and `financial_analysis = [{'monthlyBill': {'units': 120}}, {'monthlyBill': {'units': 160}}, {'monthlyBill': {'units': 140}}]`, the closest match is found to be `{'monthlyBill': {'units': 120}}`.


```
