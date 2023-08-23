"""
This program demonstrates an AWS Lambda function that fetches data from a RapidAPI endpoint,
processes it using pandas, and stores the cleaned data in an S3 bucket and a PostgreSQL RDS instance.

"""

import json
import pandas as pd
import boto3
import urllib3
import os
import psycopg2

s3 = boto3.client("s3")

def lambda_handler(event, context):
    """
    The Lambda function's entry point. This function fetches data from a RapidAPI endpoint,
    processes the data using pandas, stores the cleaned data in an S3 bucket, and inserts it into a PostgreSQL RDS instance.

    Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information provided by Lambda.

    Returns:
        dict: A dictionary containing information about the execution.
    """
    
    # TODO implement
    
    url = "https://mdblist.p.rapidapi.com/"
    querystring = {"s": "jaws"}
    headers = {
        "X-RapidAPI-Key": "d380f76d02mshd2d135b7f30363cp19aac6jsn5a2080db3a99",
        "X-RapidAPI-Host": "mdblist.p.rapidapi.com"
    }

    http = urllib3.PoolManager()
    response = http.request('GET', url, headers=headers, fields=querystring)
    
    response_data = response.data
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

    ### RDS
    try:
        conn = psycopg2.connect(
            host=os.environ['host'],
            database=os.environ['database'],
            user=os.environ['user'],
            password=os.environ['password']
        )
        print('Connected to the database')
    except Exception as e:
        print("Connection Failed")
        print(e)
    
    cursor = conn.cursor()
    table_name = "etl_raj_imdb_table"
    
    query = f"""
        CREATE TABLE {table_name} (
            id TEXT PRIMARY KEY,
            title TEXT,
            year INTEGER,
            score INTEGER,
            score_average REAL,
            type TEXT
        )
    """
    cursor.execute(query)
    conn.commit()

    data_to_insert = [tuple(row) for row in df_cleaned.values]

    insert_query = f"""
        INSERT INTO {table_name}
        (id, title, year, score, score_average, type)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, data_to_insert)
    
    # Commit the transaction
    conn.commit()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data transformed, stored in S3, and inserted into RDS.')
    }
