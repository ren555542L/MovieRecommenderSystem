import streamlit as st
import pickle
import pandas as pd
import requests
import requests
import time

def fetch_posters(movie_id):
    try:
        time.sleep(0.2)

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3d3811aad6cfd0d19fc22f614cfb2ed2&language=en-US"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=No+Poster"

        data = response.json()

        if "poster_path" not in data or data["poster_path"] is None:
            return "https://via.placeholder.com/500x750?text=No+Poster"

        return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

    except:
        return "https://via.placeholder.com/500x750?text=Error"



similarities = pickle.load(open('code\\similarity.pkl', 'rb'))

def Recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarities[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x:x[1])[1:6]
    recommended_movies = []
    posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_posters(movies.iloc[i[0]].movie_id))
    return recommended_movies, posters

movies_dict = pickle.load(open('code\\movies_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

st.title('Movicher - Recommends Movies')
selected_movie_name = st.selectbox(
    'Choose the Movie',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = Recommend(selected_movie_name)
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