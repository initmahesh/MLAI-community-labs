import re
from textblob import TextBlob
import numpy as np

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email) is not None and re.match(pattern, email):
        return "The pattern of email is valid"
    else:
        return "The pattern of email is not valid"
    
def password_strength(password):
    if len(password) < 8:
        return "Password strength is Weak"
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "Password strength is Strong"
    else:
        return "Password strength is Medium"

def calculate_entropy(temperature, delta_energy):
    return (str(delta_energy / temperature) + 'Joules/Kelvin')

def wave_speed(wavelength, frequency):
    return (str(wavelength * frequency) + "m/s")

def projectile_motion_range(v0, theta, g=9.8):
    theta_rad = theta * (3.141592653589793 / 180.0)  # Convert degrees to radians
    return (v0 ** 2) * np.sin(2 * theta_rad) / g

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def even_squares(n):
    return [x**2 for x in range(n) if x % 2 == 0]

def binary_to_decimal(binary):
    try:
        return int(binary, 2)
    except Exception as e:
        return ("Number provided is not binary")