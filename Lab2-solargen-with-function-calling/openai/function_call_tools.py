instruction1 = '''
The assistant is very good at selecting functions and summarizing the output from the functions.
'''

instruction2 = '''
If the user wants to do a sentiment analysis of the text then the assistant should call the analyze sentiment function.

If the user wants to check whether the pattern of an email is valid or not, the assistant should call the function to check for the validity of the email.

If the user wants to check the strength of the password, then the assistant should call the function password strength for checking the strength.

If the user wants to calculate the entropy, ask for the temperature and delta entropy if they are not already provided by the user, then call the function calculate entropy for entropy calculation.

If the user wants to calculate the wave speed, ask for wavelength and frequency if they are not already provided by the user, then call the function for calculating wave speed.

If the user wants to calculate the projectile motion range, the assistant should ask for the velocity and theta if they are not already provided by the user, then call the function for calculating the projectile motion range.

If the user wants to convert celcius to Fahrenheit, the assistant should ask for the temperature in Celcius or C, if it is already not provided by the user, then call the function for calculating the Farenhite temperature.

If the user wants to find all the even squares, the assistant should ask for the number till which the even squares need to be generated if it is already not provided by the user, then call the function for generating the even squares.

If the user wants to convert the binary to decimal, the assistant should ask for the binary number if it is not already provided by the user, then call the function for converting binary to decimal.

If the user wants to generate the weather forecast, the assistant should ask for the address if it is not already provided by the user, then call the function for weather forecasting. The result of the weather forecasting should be summarized properly, and the key weather terms should be indented in the new line.

If the user wants to calculate the mean or standard deviation of a list of number, the assistant should use this list for calling the function for calculating mean and standard deviation.

If the user wants to solve a quadratic equation, and provides the coefficient of x^2 or x-sqaure, x and the constant, then the assistant should take these to call the function for solving quadratic equation.

If the user wants to calculate the BMI or the body mass index, then the assistant should as for the weight in Kg or kilograms and height in meters or m, for calling the function for calculating bmi.

If the user wants to calculate the distance between two coordinates and provides the x1,y1 coordinates and x2,y2 coordinates, the assistant should take these for calling the function that calculates the distance between two points.

If the user wants to calculate the monthly loan or mortgage payment and provides the principal amount, interest rate and years, the assistant should take these for calling the function that calculates the monthly mortgage payment.
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
        },
        {
            "type": "function",
            "function": {
                "name": "weather_forecast",
                "description": "Returns the weather details based on a given address",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "address": {
                            "type": "string",
                            "description": "Address required for the weather forecasting"
                        }
                    },
                    "required": ["address"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_mean_std",
                "description": "Calculates the mean and standard deviation of a list of numbers.",
                "parameters": {
                "type": "object",
                "properties": {
                    "numbers": {
                    "type": "array",
                    "items": {"type": "number"},
                    "description": "List of numbers"
                    }
                },
                "required": ["numbers"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "solve_quadratic_equation",
                "description": "Solves a quadratic equation and returns its roots.",
                "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                    "type": "number",
                    "description": "Coefficient of x^2 or x square in the quadratic equation"
                    },
                    "b": {
                    "type": "number",
                    "description": "Coefficient of x in the quadratic equation"
                    },
                    "c": {
                    "type": "number",
                    "description": "Constant in the quadratic equation"
                    }
                },
                "required": ["a", "b", "c"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_distance",
                "description": "Calculates the distance between two points.",
                "parameters": {
                "type": "object",
                "properties": {
                    "x1": {
                    "type": "number",
                    "description": "x-coordinate of the first point"
                    },
                    "y1": {
                    "type": "number",
                    "description": "y-coordinate of the first point"
                    },
                    "x2": {
                    "type": "number",
                    "description": "x-coordinate of the second point"
                    },
                    "y2": {
                    "type": "number",
                    "description": "y-coordinate of the second point"
                    }
                },
                "required": ["x1", "y1", "x2", "y2"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_bmi",
                "description": "Calculates the Body Mass Index (BMI) based on weight and height.",
                "parameters": {
                "type": "object",
                "properties": {
                    "weight_kg": {
                    "type": "number",
                    "description": "Weight in kilograms"
                    },
                    "height_m": {
                    "type": "number",
                    "description": "Height in meters"
                    }
                },
                "required": ["weight_kg", "height_m"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_monthly_payment",
                "description": "Calculates the monthly mortgage payment.",
                "parameters": {
                "type": "object",
                "properties": {
                    "principal": {
                    "type": "number",
                    "description": "Loan amount"
                    },
                    "annual_interest_rate": {
                    "type": "number",
                    "description": "Annual interest rate"
                    },
                    "years": {
                    "type": "number",
                    "description": "Loan term in years"
                    }
                },
                "required": ["principal", "annual_interest_rate", "years"]
                }
            }
        }
    ]