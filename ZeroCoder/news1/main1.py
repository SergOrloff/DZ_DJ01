from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template('index1.html', weather=weather, news=news)


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


if __name__ == '__main__':
    app.run(debug=True)