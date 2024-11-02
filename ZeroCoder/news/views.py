from django.shortcuts import render
from . models import News_post
import requests

def home(request):
	news = News_post.objects.all()
	news1 = get_news()
	return render(request, 'news/news.html', {'news': news,  'news1': news1})

def get_news():
	api_key = "2b702542243f46be8142abcb395c343e"
	url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
	response = requests.get(url)
	return response.json().get("articles", [])

# def index(request):
# 	news1 = get_news()
# 	return render(request, 'news/news.html', {'news1': news1})