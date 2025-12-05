import pickle
import pandas as pd

# Load saved models
movies = pickle.load(open('models/movies_list.pkl', 'rb'))
similarity = pickle.load(open('models/similarity_matrix.pkl', 'rb'))

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