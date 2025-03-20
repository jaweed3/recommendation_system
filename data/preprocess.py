import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

movies_df = pd.read_csv('data/processes/movies.csv')

movies_df['year'] = movies_df['title'].str.extract(r'\((\d{4})\)').fillna('0')
movies_df['year'] = pd.to_numeric(movies_df['year'])
movies_df['title'] = movies_df['title'].str.replace(r'\s*\(\d{4}\)\s*', '', regex=True)

movies_df['genres'] = movies_df['genres'].str.replace('|', ' ')

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genres'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies_df.index, index=movies_df['title']).drop_duplicates()

os.makedirs('models', exist_ok=True)
with open('models/tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)

with open(f'models/cosine_sim.pkl', 'wb') as c:
    pickle.dump(cosine_sim, c)

with open(f'model/indices.pkl', 'wb') as i:
    pickle.dump(indices, i)

movies_df.to_csv('data/processes/movies_processed.csv', index=False)

print("Preprocessing Complete!")