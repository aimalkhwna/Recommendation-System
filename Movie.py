import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("Movie_dict.pkl", "rb"))
movies_list= pd.DataFrame(model)
similarity=pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[index]

    movie_list = sorted(
        list(enumerate(distance)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies_list.iloc[i[0]].title)

    return recommended_movies

st.title("Movie Recommendation System")
slected_movie=st.selectbox("Select a movie:", movies_list["title"].values)

if st.button("Recommend"):
    recommendations = recommend(slected_movie)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)

print(movies_list.columns)        