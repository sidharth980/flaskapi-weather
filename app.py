from flask import Flask
from flask import render_template
import requests
from flask import url_for
from flask import request
from flask import redirect

api = "9c001286164fea2ca1d75f9293eae775"

def returnWeather(cityName):
    req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api}")
    weather = req.json()
    print(weather)
    try:
        temp = weather["main"]
        tempvar = temp["feels_like"]-273.15
        return round(tempvar,2),weather['weather'][0]['description'],round(temp["temp_max"]-273.15,2),temp['humidity']
    except:
        return None

app = Flask(__name__)

@app.route("/")
def reroute():
    return redirect(url_for("main",city="london"))

@app.route("/<city>")
def main(city):
    temp,atm,maxTemp,humidity = returnWeather(city)
    if temp != None:
        return render_template("index.html",temp = temp,city = city.capitalize(),atm = atm,maxTemp = maxTemp,humidity = humidity)
    else:
        return "<h1>City Not Found<h1>"

if __name__ == "__main__":
    app.run(debug=True)
