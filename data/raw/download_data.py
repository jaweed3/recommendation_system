import os
import pandas as pd
import zipfile
import requests
from io import BytesIO

os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processes', exist_ok=True)

url = 'https://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
print('Downloading Movielens Dataset....')
response = requests.get(url)
zipfile_data = BytesIO(response.content)

with zipfile.ZipFile(zipfile_data) as zip_ref:
    zip_ref.extractall("data/raw")

print("Dataset downloaded and extracted successfully!")

print("Proceesing the dataset")
movies_df = pd.read_csv('data/raw/ml-latest-small/movies.csv')
ratings_df = pd.read_csv('data/raw/ml-latest-small/ratings.csv')

movies_df.to_csv('data/processes/movies.csv', index=False)
ratings_df.to_csv('data/processes/ratings.csv', index=False)

print("Dataset processed and saved successfully!")