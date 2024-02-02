instruction1 = '''
The assistant is very good at selecting functions and summarizing the output from the functions.
'''

instruction2 = '''
If the user wants to do a sentiment analysis of the text then the assistant should call the analyze sentiment function.

If the user wants to check whether the pattern of an email is valid or not, the assistant should call the function to check for the validity of the email.

If the user wants to check the strength of the password, then the assistant should call the function password strength for checking the strength.

If the user wants to calculate the entropy, ask for the temperature and delta entropy if they are not already provided by the user, then call the function calculate entropy for entropy calculation.

If the user wants to calculate the wave speed, ask for wavelength and frequency if theya re not already provided by the user, then call the function for calculating wave speed.
'''

tools = [
        {
            "type": "function",
            "function": {
                "name": "analyze_sentiment",
                "description": "Performs sentiment analysis of a given text",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "Text that is used for sentiment analysis",
                        }
                    },
                    "required": ["text"],
                },
            }
        },
        {
        "type":"function", 
        "function":{
                "name": "is_valid_email",
                "description": "Determines if the email follows a valid pattern or not",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email":{
                              "type":"string",
                              "description":"Email that needs to be used for performing validation"
                          }
                    },
                    "required": ["email"],
                },
            }
        },
        {
        "type":"function", 
        "function":{
                "name": "password_strength",
                "description": "Determines the strength of the password",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "password":{
                              "type":"string",
                              "description":"Password that needs to be used for performing strength check"
                          }
                    },
                    "required": ["password"],
                },
            }
        },
        {
        "type":"function", 
        "function":{
                "name": "calculate_entropy",
                "description": "Calculate the entropy using temperature and delta energy",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "temperature":{
                              "type":"number",
                              "description":"Temperature that is used for entropy calculation in Kelvin"
                          },
                        "delta_energy":{
                              "type":"number",
                              "description":"Delta Energy that is used for entropy calculation in Joules"
                          }
                    },
                    "required": ["temperature","delta_energy"],
                },
            }
        },
        {
        "type":"function", 
        "function":{
                "name": "wave_speed",
                "description": "Calculates the wave speed using wave length in meter or m and frequency in Hertz or Hz",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "wavelength":{
                              "type":"number",
                              "description":"Wavelength in meter or m that is used for wave speed calculation"
                          },
                        "frequency":{
                              "type":"number",
                              "description":"Frequency in Hertz or Hz that is used for wave speed calculation"
                          }
                    },
                    "required": ["wavelength","frequency"],
                },
            }
        },
        {
            "type": "function",
            "function": {
            "name": "projectile_motion_range",
            "description": "Calculates the horizontal range of a projectile.",
            "parameters": {
                "type": "object",
                "properties": {
                "v0": {
                    "type": "number",
                    "description": "Initial velocity (in meters per second or m/s)"
                },
                "theta": {
                    "type": "number",
                    "description": "Launch angle (in degrees)"
                },
                "g": {
                    "type": "number",
                    "description": "Acceleration due to gravity (default is 9.8 m/s^2)"
                }
                },
                "required": ["v0", "theta"]
            }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "celsius_to_fahrenheit",
                "description": "Converts temperature from Celsius to Fahrenheit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "celsius": {
                            "type": "number",
                            "description": "Temperature in Celsius or C"
                        }
                    },
                    "required": ["celsius"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "even_squares",
                "description": "Generates a list of squares of even numbers up to a given limit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "n": {
                            "type": "integer",
                            "description": "Limit for generating even squares"
                        }
                    },
                    "required": ["n"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "binary_to_decimal",
                "description": "Converts binary number to decimal",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "binary": {
                            "type": "string",
                            "description": "The binary number to be converted to decimal"
                        }
                    },
                    "required": ["binary"]
                }
            }
        }
    ]