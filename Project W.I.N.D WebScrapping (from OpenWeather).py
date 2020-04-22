#import libs
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

#url of the OpenWeather API
url = "https://api.openweathermap.org/data/2.5/onecall?lat=14.590456&lon=120.9774225&units=metric&current.dt&appid={API Key}"

#Website Actions
url = urlopen(url)
urlRead = url.read()
url.close()

#file open for insertion of data
file = 'dataset.txt'
f = open(file, 'w')

#writes the headers for the dataset
headers = "date/time, temp, feels_like, humidity, wind_speed\n"
f.write(headers)

#BS Actions
#parses html into a soup data structure to traverse html.
html = bs(urlRead, "html.parser")
