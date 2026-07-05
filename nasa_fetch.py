import requests
import json
import boto3

API_KEY = "w7AKv07MEk4vpPoEQ0rD1fm1Gf7cK0IXwXYXahfW"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
response = requests.get(url)
data = response.json()

print("Title:", data["title"])
print("Date:", data["date"])

# Save to S3
s3 = boto3.client("s3", region_name="us-east-1")
s3.put_object(
    Bucket="nasa-space-data-gaya3",
    Body=json.dumps(data),
    Key="nasa_data.json"
)

print("Data saved to S3!")
