import pickle
import pandas as pd
import ast
import os
import gdown

from data_load import get_movie


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

FILE_ID = "1qpAcZ56oo14B1qbeuDJN893N4wKVlnuL"

if not os.path.exists("similarity.pkl"):
    print("Downloading similarity.pkl...")

    gdown.download(
        f"https://drive.google.com/uc?id={FILE_ID}",
        "similarity.pkl",
        quiet=False
    )

similarity = pickle.load(open("similarity.pkl", "rb"))



def recommend(movie, top_n=50):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        enumerate(similarity[movie_index]),
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for idx, score in distances[1:]:

        movie_id = int(movies.iloc[idx].movie_id)

        details = get_movie(movie_id)

        if details is None:
            continue

        recommendations.append({

            "movie_id": movie_id,

            "title": movies.iloc[idx].title,

            "poster": details["poster"],

            "overview": details["overview"],

            "release_date": details["release_date"],

            "rating": details["rating"],

            "votes": details["votes"],

            "popularity": details["popularity"],

            "cast": details["cast"],

            "trailer": details["trailer"],

            "similarity": float(score),

            "genres": details["genres"],

            "language": movies.iloc[idx].original_language,

            "runtime": details["runtime"]

        })

        if len(recommendations) >= top_n:
            break

    return recommendations