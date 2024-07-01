# api/views.py
from django.http import JsonResponse
import requests
import os
from django.conf import settings

def get_client_ip(request):
    """Get the client's IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# def get_weather_and_location(ip):
#     """Get weather and location information using WeatherAPI."""
#     weatherapi_key = settings.WEATHERAPI_KEY

#     # Get weather and location info from WeatherAPI
#     weather_url = f"http://api.weatherapi.com/v1/current.json?key={weatherapi_key}&q={ip}&aqi=no"
#     weather_response = requests.get(weather_url).json()
    
#     city = weather_response['location']['name']
#     temperature = weather_response['current']['temp_c']

#     return city, temperature

def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = get_client_ip(request)
    # city, temperature = get_weather_and_location(client_ip)
    
    response_data = {
        "client_ip": client_ip,
        # "location": city,
        # "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    }
    return JsonResponse(response_data)
