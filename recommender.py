import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load processed data
movies = pd.read_pickle('models/movies_processed.pkl')

print("Movies loaded:", movies.shape)
print(movies.head())

# Initialize CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

# Convert tags to vectors
vectors = cv.fit_transform(movies['tags']).toarray()

print("\nVectors shape:", vectors.shape)
print("Each movie is now represented by", vectors.shape[1], "features")

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

print("\nSimilarity matrix shape:", similarity.shape)
print("This is a", similarity.shape[0], "x", similarity.shape[1], "matrix")

# Function to recommend movies
def recommend(movie_title):
    """
    Recommends 5 similar movies based on the given movie title
    """
    # Check if movie exists
    if movie_title not in movies['title'].values:
        return f"Movie '{movie_title}' not found in database"
    
    # Get the index of the movie
    movie_index = movies[movies['title'] == movie_title].index[0]
    
    # Get similarity scores for this movie with all others
    distances = similarity[movie_index]
    
    # Sort and get top 6 (including the movie itself)
    # We use enumerate to keep track of indices
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    # Print recommended movies
    print(f"\nMovies similar to '{movie_title}':\n")
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        print(f"  - {movies.iloc[i[0]].title}")
    
    return recommended_movies

# Test the recommender
if __name__ == "__main__":
    # Test with Avatar
    recommend('Avatar')
    
    print("\n" + "="*50 + "\n")
    
    # Test with another movie
    recommend('The Dark Knight')

    # Save similarity matrix and movies dataframe
pickle.dump(similarity, open('models/similarity_matrix.pkl', 'wb'))
pickle.dump(movies, open('models/movies_list.pkl', 'wb'))

print("\nModels saved successfully!")