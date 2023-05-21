import streamlit as st
import pickle as pkl
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

movies = pkl.load(open("movies.pkl", "rb"))
similarity = pkl.load(open("similarity.pkl", "rb"))


movies_list = movies["title"]


def recommend_movies(movie):
    
    index = movies_list[movies_list == movie].index[0]
    
    distances = similarity[index]
    title_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    print("Title list")
    #8265bd1679663a7ea12ac168da84d2e8

    print(title_list)
    recommend_movies = []
    movies_image = []
    for i in title_list:

        recommend_movies.append(movies_list[i[0]])
        movie_id = (movies.iloc[i[0]].id)
        movies_image.append(fetch_poster(movie_id))

        
    return recommend_movies, movies_image


st.title("Movie Recommendation System")

# def recommend(movie):


    

option = st.selectbox(
    'Choose a movie for Recommmendation',
       movies_list)

if st.button("Recommend"):
    names, posters = recommend_movies(option)
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
