import pickle
import pandas as pd
from tmdb_service import fetch_movie_details
import time

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

all_movies = []

total = len(movies)

for i, row in movies.iterrows():

    movie_id = int(row.movie_id)
    title = row.title

    print(f"{i+1}/{total}  {title}")

    details = None

    # Retry up to 3 times
    for _ in range(3):

        details = fetch_movie_details(movie_id)

        if details:
            break

        print("Retrying...", movie_id)
        time.sleep(2)

    if details is None:
        details = {}

    movie = {

        "movie_id": movie_id,
        "title": title,

        "poster": details.get("poster"),
        "backdrop": details.get("backdrop"),
        "overview": details.get("overview"),
        "release_date": details.get("release_date"),
        "rating": details.get("rating"),
        "votes": details.get("votes"),
        "popularity": details.get("popularity"),
        "runtime": details.get("runtime"),
        "genres": details.get("genres"),
        "trailer": details.get("trailer"),
        "cast": details.get("cast")

    }

    all_movies.append(movie)

pickle.dump(
    all_movies,
    open("movies_enriched.pkl", "wb")
)

print("\nDONE ✅")