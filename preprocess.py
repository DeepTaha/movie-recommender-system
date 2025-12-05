import pandas as pd
import numpy as np
import json

# Load datasets
movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')

print("Movies loaded:", movies.shape)
print("Credits loaded:", credits.shape)

# Merge on title or id
movies = movies.merge(credits, on='title')

print("After merge:", movies.shape)
print(movies.head(2))

# Keep only useful columns
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

print("\nColumns we're using:")
print(movies.columns)
print("\nShape:", movies.shape)

# Check missing values
print("\nMissing values:")
print(movies.isnull().sum())

# Drop rows with missing values
movies.dropna(inplace=True)

print("\nAfter dropping nulls:", movies.shape)

# Function to extract names from JSON
def extract_names(obj):
    """Extract 'name' field from list of dictionaries"""
    names = []
    for item in json.loads(obj):
        names.append(item['name'])
    return names

# Function to extract top 3 cast members
def extract_cast(obj):
    """Extract top 3 cast names"""
    names = []
    counter = 0
    for item in json.loads(obj):
        if counter < 3:
            names.append(item['name'])
            counter += 1
        else:
            break
    return names

# Function to extract director from crew
def extract_director(obj):
    """Extract director name from crew"""
    for item in json.loads(obj):
        if item['job'] == 'Director':
            return [item['name']]
    return []
# Apply extraction functions
# Apply functions to extract data
movies['genres'] = movies['genres'].apply(extract_names)
movies['keywords'] = movies['keywords'].apply(extract_names)
movies['cast'] = movies['cast'].apply(extract_cast)
movies['crew'] = movies['crew'].apply(extract_director)

# Rename crew to director for clarity
movies.rename(columns={'crew': 'director'}, inplace=True)

print("\nAfter extraction:")
print(movies.head(1))

# Function to remove spaces from names
def remove_spaces(words_list):
    """Remove spaces from list of strings"""
    return [word.replace(" ", "") for word in words_list]

# Apply to all list columns
movies['genres'] = movies['genres'].apply(remove_spaces)
movies['keywords'] = movies['keywords'].apply(remove_spaces)
movies['cast'] = movies['cast'].apply(remove_spaces)
movies['director'] = movies['director'].apply(remove_spaces)

print("\nAfter removing spaces:")
print(movies[['title', 'genres', 'cast', 'director']].head(1))

# Convert overview to list of words (split and remove spaces)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

print("\nOverview as list:")
print(movies['overview'].head(1))

# Create tags by combining all features
movies['tags'] = movies['genres'] + movies['keywords'] + movies['cast'] + movies['director'] + movies['overview']

print("\nTags created:")
print(movies['tags'].head(1))

# Convert tags list to lowercase string
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x).lower())

print("\nTags as string:")
print(movies[['title', 'tags']].head(1))

# Keep only needed columns
movies_final = movies[['movie_id', 'title', 'tags']]

print("\nFinal dataset:")
print(movies_final.head())
print("\nShape:", movies_final.shape)

# Save to pickle file for later use
movies_final.to_pickle('models/movies_processed.pkl')
print("\nProcessed data saved to models/movies_processed.pkl")