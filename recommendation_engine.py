import pickle
import pandas as pd
import os

def load_models():
    """Load models, generate if they don't exist"""
    if not os.path.exists('models/movies_list.pkl'):
        # Generate models if they don't exist
        print("Generating models for the first time...")
        import preprocess
        import recommender
        print("Models generated successfully!")
    
    # Now load the models
    movies = pickle.load(open('models/movies_list.pkl', 'rb'))
    similarity = pickle.load(open('models/similarity_matrix.pkl', 'rb'))
    return movies, similarity

# Load models at module import
movies, similarity = load_models()

def get_recommendations(movie_title):
    """
    Returns list of 5 recommended movies
    """
    # Check if movie exists
    if movie_title not in movies['title'].values:
        return []
    
    # Get movie index
    movie_index = movies[movies['title'] == movie_title].index[0]
    
    # Get similarity scores
    distances = similarity[movie_index]
    
    # Get top 5 similar movies (excluding the input movie)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    # Return list of movie titles
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    
    return recommended_movies