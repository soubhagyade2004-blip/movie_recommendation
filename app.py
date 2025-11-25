import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

PLACEHOLDER = "https://via.placeholder.com/500x750?text=No+Image"
TMDB_BASE = "https://api.themoviedb.org/3"
TMDB_KEY = "08612c0f4818feac4c0f12f901398960"

def session_with_retries(total_retries=3, backoff_factor=0.3, status_forcelist=(429, 500, 502, 503, 504)):
    s = requests.Session()
    retries = Retry(total=total_retries, backoff_factor=backoff_factor, status_forcelist=status_forcelist, allowed_methods=frozenset(["GET","POST"]))
    s.mount("https://", HTTPAdapter(max_retries=retries))
    s.mount("http://", HTTPAdapter(max_retries=retries))
    return s

_session = session_with_retries()

def fetch_poster(movie_id):
    if not movie_id:
        return PLACEHOLDER
    try:
        resp = _session.get(f"{TMDB_BASE}/movie/{movie_id}", params={"api_key": TMDB_KEY, "language": "en-US"}, timeout=8)
        if resp.status_code != 200:
            return PLACEHOLDER
        data = resp.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return PLACEHOLDER
    except requests.exceptions.RequestException:
        return PLACEHOLDER

def recommend(movie):
    try:
        movie_index = movies.index[movies["title"] == movie][0]
    except Exception:
        return [], []
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        idx = i[0]
        movie_id = movies.iloc[idx]["id"]
        recommended_movies.append(movies.iloc[idx]["title"])
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

@st.cache_data
def load_data():
    movie_dict = pickle.load(open("movie_dict.pkl", "rb"))
    movies_df = pd.DataFrame(movie_dict)
    sim = pickle.load(open("similarity.pkl", "rb"))
    return movies_df, sim

movies, similarity = load_data()

st.title("Movie Recommendation System")
selected_movie_name = st.selectbox("Select Movie", movies["title"].values)
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    if len(names) >= 5:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])
    else:
        st.error("Could not find recommendations for the selected movie.")

