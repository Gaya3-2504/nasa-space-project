import json
import urllib.request
import boto3
import os

def lambda_handler(event, context):
    api_key = os.environ.get("NASA_API_KEY")
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    s3 = boto3.client("s3", region_name="us-east-1")
    s3.put_object(
        Bucket="nasa-space-data-gaya3",
        Body=json.dumps(data),
        Key=f"raw/{data['date']}.json"
    )

    return {"statusCode": 200, "body": f"Saved {data['date']}"}
