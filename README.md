# Recommendation System with TensorFlow (Zero to Deployment)

## Overview
This project is a **content-based recommendation system** built using **TensorFlow**. It takes the **MovieLens Small dataset** and trains a recommendation model from scratch, then deploys it as a web service.

## Features
- **Data Preprocessing**: Cleaning and preparing MovieLens Small dataset.
- **Model Building**: Using TensorFlow to create a recommendation model.
- **Training & Evaluation**: Optimizing performance with different hyperparameters.
- **Deployment**: Serving the model via **FastAPI** or **Flask**.

## Dataset
We use the **MovieLens Small (ml-latest-small)** dataset, which contains **100,000 ratings** across **9,000 movies** from **600 users**. It includes:
- `ratings.csv` – user ratings for movies.
- `movies.csv` – metadata of movies (title, genre, etc.).

## Tech Stack
- **Python**
- **TensorFlow & Keras**
- **Pandas & NumPy**
- **Scikit-learn**
- **FastAPI/Flask** (for API deployment)
- **Docker** (optional for containerization)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/recommendation-system.git
   cd recommendation-system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Model Training
Run the training script:
```bash
python train.py
```
This will:
- Load and preprocess the dataset
- Train the TensorFlow model
- Save the trained model to disk

## Deployment
1. Start the API server:
   ```bash
   uvicorn app:app --reload
   ```
2. Access the API at `http://127.0.0.1:8000`
3. Example API call:
   ```bash
   curl -X GET "http://127.0.0.1:8000/recommend?user_id=1"
   ```
   This returns recommended movies for `user_id=1`.

## Future Improvements
- Integrate **Collaborative Filtering** for better recommendations.
- Implement **Hybrid Recommendation** combining multiple methods.
- Deploy on **Cloud (AWS/GCP/Azure)** for scalability.

## Contributing
Feel free to fork this repository and submit a pull request if you have any improvements!

## License
This project is licensed under the **MIT License**.

