import pandas as pd
import numpy as np
from src.models.recommendation_model import ContentBasedRecommender
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.makedirs('reports/figures', exist_ok=True)

ratings_df = pd.read_csv('data/processed/ratings.csv')
recommender = ContentBasedRecommender()
popular_movies = ratings_df.groupby('movieId').count().sort_values('rating', ascending=False).head(20)
popular_movies_ids = popular_movies.index.tolist()

movies_df = pd.read_csv('data/processed/movies_processed.csv')
popular_movie_titles = movies_df[movies_df['movieId'].isin(popular_movies_ids)]['title'].tolist()

results = []
for title in popular_movie_titles:
    recommendations = recommender.get_recommendations(title, top_n=5)
    if recommendations:
        avg_similarity = np.mean([rec['similarity_score'] for rec in recommendations])
        results.append({
            'movie': title,
            'avg_similarity': avg_similarity,
            'recommendations': [rec['title'] for rec in recommendations]
        })

results_df = pd.DataFrame(results)

plt.figure(fisize=(12, 8))
sns.barplot(x='avg_similarity', y='movie', data=results_df)
plt.title('Average Similarity Score of Recommendations for Popular Movies')
plt.xlabel('Average Similarity Score')
plt.ylabel('Movie')
plt.tight_layout()
plt.savefig('reports/figures/similarity_score.png')

print("Evaluation Results")
for _, row in results_df.iterrows():
    print(f"Movie: {row['movie']}")
    print(f"Average Similarity Score: {row['avg_similarity']}")
    print(f"Recommendations: {', '.join(row['recommendations'])}")
    print("-"*50)

results_df.to_csv('reports/evaluation_metrics.csv')
print("Evaluation Complete! Results Saved to `reports/evaluation_metrics.csv` ")