from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'd5d855d055b434209d70bb7b8f8cc00b'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()
        
        if response.get('cod') != 200:
            weather = "City not found!"
        else:
            weather = {
                'city': response['name'],
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon']
            }
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
