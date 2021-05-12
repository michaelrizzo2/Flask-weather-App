#import statements
import requests
import os
from flask import Flask,render_template,request

#Setting up the app and the needed options
app=Flask(__name__)
app.config['DEBUG']=True



#Setting up the routes,
@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        new_city=request.form.get('city')

    if new_city:
       pass 
    #This is where we will get all of the cities for the next query

    #This will be for getting all of the weather data
    url=f'http://api.openweathermap.org/data/2.5/weather?q={new_city}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    #This will be for putting the data insode of an json object
    for city in cities:
        #Setting up the json 
        city_json_object=requests.get(url.format(city.name)).json()
        #putting json data into weather dictionary
        weather={
            'city':city.name,
            'temperature':city_json_object['main']['temp'],
            'description':city_json_object['weather'][0]['description'],
            'icon':city_json_object['weather'][0]['icon']
        }
        #adding new dictionary to the list.

    return render_template('weather.html',weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
