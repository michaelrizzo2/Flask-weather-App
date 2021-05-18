#import statements
import requests
import os
from flask import Flask,render_template,request
from firebase import firebase
from firebase_admin import credentials,firestore 
import firebase_admin
#setting up firebase database link
cred = credentials.Certificate("../../service key.json")
firebase_admin.initialize_app(cred)
firestore_database=firestore.client()
#Setting up the app and the needed options
app=Flask(__name__)



#Setting up the routes,
@app.route('/',methods=["POST"])
def home():
    if request.method=="POST":
        new_city=request.form.get('city')
        print(new_city)

    #This will be for getting all of the weather data
    url=f'http://api.openweathermap.org/data/2.5/weather?q={new_city}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    #This will be for putting the data insode of an json object
    #Setting up the json 
    city_json_object=requests.get(url.format(new_city.name)).json()
    #putting json data into weather dictionary
    weather={
        'city':new_city,
        'description':city_json_object['weather'][0]['description'],
        'temperature':city_json_object['main']['temp'],
        }
    firestore_database.collection(u'weather').add(weather)

    return render_template('weather.html',weather_data=weather)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
