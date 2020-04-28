#import the necessary libs
import pandas as pd
import datetime
from csv import writer

#to append data to the next row of the existing dataset(.csv)
def appendrow(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

#takes the url
url = "https://api.openweathermap.org/data/2.5/onecall?lat=14.590456&lon=120.9774225&units=metric&current.dt&appid=40b08dff1c7e4fc895c7a3d3d9978d92"
jsonData = requests.get(url).json()

# get from dataframe and jsondata
lat,lon = jsonData['lat'],jsonData['lon']
tz = jsonData['timezone']
df = jsonData['current']
dt = df['dt'] 
temp = df['temp']
feels = df['feels_like'] 
pres = df['pressure'] 
hum = df['humidity']

#converts dt(a unix timestamp format) into GMT+8
dt = datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S')
print(dt)

#place data into a list
weatherdata = [lat,lon,tz,dt,temp,feels,pres,hum]
#append list into dataset
appendrow('weather.csv', weatherdata)
