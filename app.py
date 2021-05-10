#import statements
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

#Setting up the app and the needed options
app=Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

#Setting up the database
my_database=SQLAlchemy(app)

#Setting up sql fields
class City(my_database.model):
    id=my_database.column(my_database.Integer,primary_key=True)
    name=my_database.column(my_database.String(50),nullable=False)

#Setting up the routes,
@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        new_city=request.form.get('city')

        if new_city:
            new_city_object=City(name=new_city)
            #Adding new information to the database
            my_database.session.add(new_city_object)
            my_database.session.commit()
    
    #This is where we will get all of the cities for the next query
    cities=City.query.all()

    #This will be for getting all of the weather data
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    #This will hold all of the weather data
    weather_data=[]

