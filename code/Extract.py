"""
This program demonstrates the creation of an AWS Lambda function to import data from an API and store it in an S3 bucket.

"""

import json
import boto3
import urllib3

# Initialize AWS S3 client
s3 = boto3.client("s3")

def lambda_handler(event, context):
    """
    The Lambda function's entry point.

    Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information provided by Lambda.

    Returns:
        dict: A dictionary containing information about the execution.
    """

    # URL and query parameters for the API request
    url = "https://mdblist.p.rapidapi.com/"
    querystring = {"s": "jaws"}
    
    # Headers required for the RapidAPI request
    headers = {
        "X-RapidAPI-Key": "d380f76d02mshd2d135b7f30363cp19aac6jsn5a2080db3a99",
        "X-RapidAPI-Host": "mdblist.p.rapidapi.com"
    }

    # Create an HTTP connection pool manager
    http = urllib3.PoolManager()
    
    # Make a GET request to the API
    response = http.request('GET', url, headers=headers, fields=querystring)
    
    # Extract the response data
    response_data = response.data
    
    # Parse the JSON response data
    parsed_response = json.loads(response_data)
    
    # Upload the raw data to an S3 bucket
    s3.put_object(Body=response_data, Bucket='apprentice-training-ml-raj-raw', Key='raw_data.json')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data imported successfully and stored in S3.')
    }
