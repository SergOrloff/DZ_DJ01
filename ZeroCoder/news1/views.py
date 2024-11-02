from django.shortcuts import render
import requests

def get_weather(city):
    API_KEY = "493015191bcb9ed0d50cde1ac4c34ae7"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "2b702542243f46be8142abcb395c343e"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get("articles", [])

def index(request):
    weather = None
    news = None
    if request.method == 'POST':
        city = request.POST.get('city')
        weather = get_weather(city)
        news = get_news()
    return render(request, 'news1/index1.html', {'weather': weather, 'news': news})