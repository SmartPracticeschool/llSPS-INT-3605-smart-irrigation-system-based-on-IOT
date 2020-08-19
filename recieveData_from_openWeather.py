import requests

api_address='https://api.openweathermap.org/data/2.5/weather?appid=b5693942990bbaa7124e38ca11d5131a&q='

city=input("city name :")

url = api_address + city

json_data = requests.get(url).json()

print(json_data)

