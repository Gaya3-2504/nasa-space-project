import requests
import json
import boto3

import os
API_KEY = os.environ.get("NASA_API_KEY")

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
