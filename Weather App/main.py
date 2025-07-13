# weather app show a specific city weather
import requests
import json
import win32com.client as wincom

api_key = 'e8f8238f94e74c13ae370416251307'
speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the name of city \n")

url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

req = requests.get(url)
# print(req.text)
# print(type(req.text))  # the return type is string


# now to convert into a dictory type

weatherDic = json.loads(req.text)
# print(weatherDic["location"]["region"])
temp_c = weatherDic["current"]["temp_c"]

print(f"The current weather in {city} is {temp_c}")
text = f"The current weather in {city} is {temp_c}"
speak.Speak(text)
