"""
This program demonstrates an AWS Lambda function that fetches data
from a RapidAPI endpoint, processes it, and stores the transformed 
data in an S3 bucket.
"""

import json
import pandas as pd
import boto3
import urllib3

# Initialize AWS S3 client
s3 = boto3.client("s3")

def lambda_handler(event, context):
    """
    The Lambda function's entry point. This function fetches data from a RapidAPI endpoint,
    processes the data using pandas, and stores the cleaned data in an S3 bucket.

    Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information provided by Lambda.

    Returns:
        dict: A dictionary containing information about the execution.
    """

    # URL and query parameters for the API request
    url = "https://mdblist.p.rapidapi.com/"
    querystring = {"s": "jaws"}
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

    # Transformation of data

    # Extract 'search' list from the data and create a DataFrame
    search_results =  parsed_response['search']
    df = pd.DataFrame(search_results)
    
    # Drop unnecessary columns
    df_cleaned = df.drop(['tvdbid', 'imdbid', 'tmdbid', 'traktid'], axis=1)
    
    # Fill missing data for specific rows
    df_cleaned.at[47, 'year'] = 2013
    df_cleaned.at[13, 'year'] = 1975
    
    # Convert year to datetime format
    df_cleaned['year'] = pd.to_datetime(df_cleaned['year'], format='%Y').dt.year
    
    # Fill missing data in the 'score_average' column with the mean value
    df_cleaned['score_average'].fillna(df_cleaned['score_average'].mean(), inplace=True)
    
    # Convert cleaned DataFrame to JSON format
    cleaned_json = df_cleaned.to_json(orient='records')
    
    # Store the cleaned JSON data in an S3 bucket
    s3.put_object(Body=cleaned_json, Bucket='apprentice-training-ml-raj-clean', Key='cleaned_data.json')

    return {
        'statusCode': 200,
        'body': json.dumps('Data transformed and stored in S3.')
    }
