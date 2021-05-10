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
