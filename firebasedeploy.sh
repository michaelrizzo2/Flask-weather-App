
#This will build the images 
gcloud builds submit --tag gcr.io/flask-weather-app-937e6/myflask
#This will deploy the image
gcloud beta run deploy --image gcr.io/flask-weather-app-937e6/myflask
#This will deploy the image to firebase
firebase deploy
