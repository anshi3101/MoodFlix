import pickle
import pandas as pd
import requests
import time
import ast
from tmdb_service import fetch_movie_details

# Load Data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

tmdb = pd.read_csv("tmdb_5000_movies.csv")


def extract_genres(text):
    try:
        genres = ast.literal_eval(text)
        return [g["name"] for g in genres]
    except:
        return []


tmdb["genres"] = tmdb["genres"].apply(extract_genres)

movies = movies.merge(
    tmdb[["title", "genres", "original_language", "runtime"]],
    on="title",
    how="left"
)

similarity = pickle.load(open("similarity.pkl", "rb"))

API_KEY = "32f8ac1a21f52f177d724040cdf7a57d"
session = requests.Session()

def recommend(movie, top_n=50):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        enumerate(similarity[movie_index]),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in distances[1:1000]:

        idx = i[0]

        movie_id = movies.iloc[idx].movie_id

        details = fetch_movie_details(movie_id)

        recommendations.append({

            "movie_id": movie_id,

            "title": movies.iloc[idx].title,

            "poster": details["poster"] if details else None,

            "overview": details["overview"] if details else "",

            "release_date": details["release_date"] if details else "",

            "rating": details["rating"] if details else 0,

            "votes": details["votes"] if details else 0,

            "popularity": details["popularity"] if details else 0,

            "cast": details["cast"] if details else [],

            "trailer": details["trailer"] if details else None,

            "similarity": float(i[1]),

            "genres": details["genres"] if details else movies.iloc[idx].genres,

            "language": movies.iloc[idx].original_language,

            "runtime": details["runtime"] if details else movies.iloc[idx].runtime

        })

    return recommendations[:top_n]