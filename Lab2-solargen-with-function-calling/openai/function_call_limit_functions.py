import re
from textblob import TextBlob
import numpy as np
from dotenv import load_dotenv
import os
import urllib3
import json
import cmath
import math
load_dotenv()

GOOGLE_API = os.getenv('GOOGLE_API')
WEATHER_KEY = os.getenv('WEATHER_KEY')

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
    
def weather_forecast(address):
    try:
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
            lat,lng = location['lat'], location['lng']
        else:
            return "Could not fetch coordinates"

        weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={WEATHER_KEY}"
        response = http.request(
                'GET',
                weather_api
            )
        if response.status == 200:
            response = response.data
            response = response.decode('utf-8')
            response = json.loads(response)
            details = [response.get('weather'), response.get('main'),response.get('visibility'),response.get('wind'),response.get('clouds')]
            return details
        else:
            return "Could not fetch weather details for this location"
    except Exception as e:
        print("Something went wrong :\n"+e)

def calculate_mean_std(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_deviation = variance ** 0.5
    return [{'mean':mean, 'std_deviation':std_deviation}]


def solve_quadratic_equation(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return [{'root 1':root1, 'root 2':root2}]

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_payments = years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    return monthly_payment