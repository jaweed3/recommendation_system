import tensorflow as tf
import numpy as np
import pandas as pd
import pickle
import os

class ContentBasedRecommender:
    def __init__(self, model_path='models'):
        self.model_path = model_path
        self.load_data()
        self.build_model()

    def load_data(self):
        self.movie_df = pd.read_csv('data/processes/movies_processed.csv')
        with open(os.path.join(self.model_path, 'cosine_sim.pkl'), 'rb') as f:
            self.cosine_sim = pickle.load(f)

        with open(os.path.join(self.model_path, 'indices.pkl'), 'rb') as f:
            self.indices = pickle.load(f)

    def build_model(self):
        movie_input = tf.keras.layers.input(shape=(1,), name='movie_input')
        cosine_sim_tensor = tf.constant(self.cosine_sim, dtype=tf.float32)

        self.model = tf.keras.Model(inputs=movie_input, outputs=movie_input)

    def get_recommendations(self, title, top_n=10):
        if title not in self.indices:
            return []
        
        idx = self.indices[title]

        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[1:top_n+1]

        movie_indices = [i[0] for i in sim_scores]

        recommendations = self.movies_df.iloc[movie_indices][['title', 'genres', 'year']]
        recommendations['similarity_score'] = [i[1] for i in sim_scores]

        return recommendations.to_dict