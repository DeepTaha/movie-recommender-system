import pandas as pd

# Load the datasets
movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')

# Check the shape
print("Movies shape:", movies.shape)
print("Credits shape:", credits.shape)

# Check columns
print("\nMovies columns:")
print(movies.columns)

print("\nCredits columns:")
print(credits.columns)

# Check specific columns
print("\n--- Sample Data ---")
print("\nGenres (first movie):")
print(movies['genres'].iloc[0])

print("\nKeywords (first movie):")
print(movies['keywords'].iloc[0])

print("\nOverview (first movie):")
print(movies['overview'].iloc[0])

print("\nCast (first movie):")
print(credits['cast'].iloc[0])