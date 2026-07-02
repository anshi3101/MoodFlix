import ast
import pandas as pd

from genre_profiles import COMPANION_GENRES


movies = pd.read_csv("tmdb_5000_movies.csv")



def extract_genres(text):

    try:
        genres = ast.literal_eval(text)
        return [genre["name"] for genre in genres]

    except:
        return []


movies["genres"] = movies["genres"].apply(extract_genres)
movies["vote_average"] = movies["vote_average"].fillna(0)
movies["vote_count"] = movies["vote_count"].fillna(0)
movies["runtime"] = movies["runtime"].fillna(0)
movies["original_language"] = movies["original_language"].fillna("Unknown")


def companion_recommend(companion, top_n=20):

    if companion not in COMPANION_GENRES:
        return []

    profile = COMPANION_GENRES[companion]

    recommendations = []

    for _, row in movies.iterrows():

        genre_score = 0

        for genre in row["genres"]:
            genre_score += profile.get(genre, 0)

        if genre_score == 0:
            continue


        rating_score = row["vote_average"]

        vote_bonus = min(row["vote_count"] / 1000, 10)

        final_score = (
            genre_score * 2
            + rating_score
            + vote_bonus
        )

        recommendations.append({

            "title": row["title"],

            "genres": row["genres"],

            "genre_score": genre_score,

            "rating": rating_score,

            "votes": row["vote_count"],

            "runtime": row["runtime"],

            "language": row["original_language"],

            "final_score": round(final_score, 2)

        })

    recommendations = sorted(

        recommendations,

        key=lambda x: x["final_score"],

        reverse=True

    )

    return recommendations[:top_n]

def companion_filter(content_movies, companion, top_n=15):


    #Rerank content_based recommendations according to user's companion

    if companion not in COMPANION_GENRES:
        return content_movies[:top_n]

    profile = COMPANION_GENRES[companion]

    filtered_movies = []

    for movie in content_movies:

        # genres are already coming from content_based.py
        genres = movie.get("genres", [])

        companion_score = 0

        for genre in genres:
            companion_score += profile.get(genre, 0)

        movie["companion_score"] = companion_score

        filtered_movies.append(movie)

    # Rerank
    filtered_movies.sort(
        key=lambda x: (
            x["companion_score"],
            x["similarity"]
        ),
        reverse=True
    )

    return filtered_movies[:top_n]