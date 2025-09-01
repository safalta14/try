from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
import requests
from .models import City
from django.utils import timezone

# 🌤️ Homepage view
def weather(request):
    return render(request, "index.html")

# 🌍 Handles city search and weather API call
def calling(request):
    if request.method == "GET":
        city = request.GET.get('city')  # get city from URL

        if city:
            print(f"Request method: {request.method}, City param: {city}")
            city_name = city.strip().title()  # normalize input
            print(f"Normalized input: {city_name}")

            # 🌦️ Fetch weather data from OpenWeatherMap
            api_key = "3cf4d429e31906f1c566d3d8b9b0dea8"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                # ✅ Save city only if API confirms it exists
                try:
                    city_obj, created = City.objects.get_or_create(name=city_name)
                    city_obj.searched_at = timezone.now()
                    city_obj.save()
                    print(f"Saved to DB: {city_obj.name}, searched_at: {city_obj.searched_at}")
                except Exception as e:
                    print(f"Error during city save: {e}")

                weather_info = {
                    'temperature': f"{data['main']['temp']}C",
                    'humidity': data['main']['humidity'],
                    'feels_like': data['main']['feels_like'],
                    'min_temp': data['main']['temp_min'],
                    'max_temp': data['main']['temp_max'],
                    'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
                    'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),
                    'description': [w['description'] for w in data['weather']]
                }
                return JsonResponse(weather_info)
            else:
                print(f"Weather API failed for city: {city_name}")
                return JsonResponse({"error": "City not found."}, status=404)
        else:
            print("No city provided in request.")
            return JsonResponse({"error": "City not provided."}, status=400)

# 🗂️ Lists all searched cities with timestamps
def list_cities(request):
    cities = City.objects.all().order_by('-searched_at')
    data = [
        {
            'name': city.name,
            'searched_at': city.searched_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for city in cities
    ]
    return JsonResponse(data, safe=False)