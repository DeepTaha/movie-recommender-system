import streamlit as st
import pickle
import os
from recommendation_engine import get_recommendations

# Check if models exist, if not generate them
if not os.path.exists('models/movies_list.pkl'):
    st.info("Setting up the app for the first time... This may take a minute.")
    import preprocess
    import recommender
    st.success("Setup complete!")

# Load movies list for dropdown
movies_list = pickle.load(open('models/movies_list.pkl', 'rb'))
movie_titles = movies_list['title'].values

# App title
st.title('🎬 Movie Recommender System')
st.write('Select a movie to get personalized recommendations!')

# Movie selection dropdown
selected_movie = st.selectbox(
    'Choose a movie:',
    movie_titles
)

# Recommend button
if st.button('Get Recommendations'):
    recommendations = get_recommendations(selected_movie)
    
    if recommendations:
        st.subheader(f'Movies similar to "{selected_movie}":')
        for i, movie in enumerate(recommendations, 1):
            st.write(f"{i}. {movie}")
    else:
        st.error('Movie not found!')