from django.http import JsonResponse
import requests
from django.conf import settings

def get_client_ip(request):
    #helps get the ip address of user 
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(ip):
   # i am using this code to get the location using clients IP address 
    apiip_key = settings.LOCATIONAPI_KEY
    
    location_url = f"https://apiip.net/api/check?ip={ip}&accessKey={apiip_key}"
    response = requests.get(location_url)
    data = response.json()
    
    location = data.get('location', 'Unknown location')
    return location

def get_weather(location):
  #i am using this code to get the weather
    weatherapi_key = settings.WEATHERAPI_KEY 
    
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={weatherapi_key}&q={location}&aqi=no"
    response = requests.get(weather_url)
    data = response.json()
    
    temperature = data['current']['temp_c']
    return temperature

def hello(request):
    user = request.GET.get('visitor_name', 'Guest')
    client_ip = get_client_ip(request)
    
    # Get location and weather data
    location = get_location(client_ip)
    temperature = get_weather(user)
    
    context = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {user}!, the temperature is {temperature} degrees Celsius in {location}"
    }
    return JsonResponse(context)
