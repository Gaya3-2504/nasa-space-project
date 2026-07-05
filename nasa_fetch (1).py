import requests
import json

API_KEY = "w7AKv07MEk4vpPoEQ0rD1fm1Gf7cK0IXwXYXahfW"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
response = requests.get(url)
data = response.json()

print("Title:", data["title"])
print("Date:", data["date"])
print("Explanation:", data["explanation"])
