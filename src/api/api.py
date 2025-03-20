from flask import Flask, request, jsonify
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.models.recommendation_model import ContentBasedRecommender

app = Flask(__name__)
recommender = ContentBasedRecommender()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/recommend', methods=['POST'])
def get_movies():
    movies = recommender.movie_df[['movieId', 'title', 'genres', 'year']].to_dict('records')
    return jsonify({"movies": 'movies'})

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    title = request.json.get('title', '')
    top_n = int(request.args.get('top_n', 10))

    if not title:
        return jsonify({'error': "Movie title is required"}), 400
    
    recommendations = recommender.get_recommendations(title, top_n=top_n)

    if not recommendations:
        return jsonify({'error': 'Movie Title {title} is not found'}), 404
    
    return jsonify({
        'title': title,
        'recommendations': recommendations
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', post=int(os.environ.get('PORT', 5000)))