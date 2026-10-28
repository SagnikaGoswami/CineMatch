import os
from dotenv import load_dotenv
import streamlit as st
import pickle
import requests

load_dotenv()

# configuring the page for styling
st.set_page_config(
    page_title="CineMatch | Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# loading style.css file
with open("style.css", "r", encoding="utf-8") as css_file:
    st.markdown(
        f"<style>{css_file.read()}</style>",
        unsafe_allow_html=True
    )


with open('movies.pkl', 'rb') as file:
    movies_list = pickle.load(file)

movie_titles = movies_list['title'].values

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

# fetch API key
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if not TMDB_API_KEY:
    raise ValueError("TMDB_API_KEY is missing.")

# fetch poster API
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}')
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    return "https://placehold.co/500x750?text=No+Poster"

# recommend function
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]

    distances = similarity[movie_index]

    recommended_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in recommended_indices:
        movie_id = i[0]
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Website Header
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">✦ YOUR PERSONAL MOVIE GUIDE</div>
    <h1>Discover Your Next <span>Favorite Movie.</span></h1>
    <p>
        Explore movies you'll love with our intelligent
        movie recommendation system.
    </p>
</div>
""", unsafe_allow_html=True)


# Original selection logic
left, center, right = st.columns([1, 3, 1])

with center:
    selected_movie_name = st.selectbox(
        '🎥 Which movie would you like recommendations for?',
        movie_titles
    )

    recommend_button = st.button(
        'Recommend',
        use_container_width=True
    )

if recommend_button:
    names, posters = recommend(selected_movie_name)

    st.markdown(
        '<h2 class="results-title">✨ Recommended For You</h2>',
        unsafe_allow_html=True
    )

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, use_container_width=True)
            st.write(name)
