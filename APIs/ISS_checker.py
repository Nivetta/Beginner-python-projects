# importing the dependancies
import requests
from datetime import datetime
import smtplib
import time

# declaring constants
my_email = "yoshiii6601@gmail.com"
password = "n6i6v0i1tta!"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

# fn to check if ISS is withing viewing range
def is_iss_overhead():
    # requesting the external system for data using API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    #Your position is within +5 or -5 degrees of the ISS position.
    if iss_latitude in range(MY_LAT-5,MY_LAT+6) and iss_longitude in range(MY_LONG-5,MY_LONG+6):
        return True
  
# checking if it is night time so that ISS can be viewed
def night_time():    
    
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    
    # requesting the external system for data using API
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    # programs keeps running in the bg every 60 secs to check position of ISS
    time.sleep(60)
    if is_iss_overhead() and night_time():
        # setting up connection and sending email
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttlas()
        connection.login(my_email,password)
        connection.sendmail(my_email, my_email, msg="Subject: Look Up ^^\n\nThe ISS is ablove you in the sky")
        
                                  



