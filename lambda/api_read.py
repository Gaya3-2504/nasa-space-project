import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("apod-history")

    # Check if the URL had a date in it, like /apod/2026-07-06
    path_params = event.get("pathParameters") or {}
    date = path_params.get("date")

    if date:
        response = table.get_item(Key={"date": date})
        item = response.get("Item")
    else:
        # No date given - just grab the most recent one
        response = table.scan()
        items = response.get("Items", [])
        item = sorted(items, key=lambda x: x["date"], reverse=True)[0] if items else None

    if not item:
        return {
            "statusCode": 404,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Not found"})
        }

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(item)
    }
