from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "insert your api key here"

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    weather = {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "description": data["current"]["condition"]["text"],
            "icon": data["current"]["condition"]["icon"],
        }
    return weather    



@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
       city = request.form.get("city") 
       if city:
          weather = get_weather(city) 
          if weather:
              return render_template("weather.html", weather=weather)
          else:
              return render_template("home.html", error="City not found!")
    return render_template("home.html")          

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
