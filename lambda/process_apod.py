import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("apod-history")

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    response = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(response["Body"].read())

    table.put_item(Item={
        "date": data["date"],
        "title": data["title"],
        "explanation": data["explanation"],
        "image_url": data.get("url", "")
    })

    return {"statusCode": 200, "body": f"Saved {data['date']} to DynamoDB"}
