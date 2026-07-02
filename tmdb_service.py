import requests
from functools import lru_cache

API_KEY = "32f8ac1a21f52f177d724040cdf7a57d"

BASE_URL = "https://api.themoviedb.org/3"

IMAGE_URL = "https://image.tmdb.org/t/p/w500"


@lru_cache(maxsize=5000)
def fetch_movie_details(movie_id):

    url = f"{BASE_URL}/movie/{movie_id}"

    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "append_to_response": "videos,credits"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()

        poster = None

        if data.get("poster_path"):

            poster = IMAGE_URL + data["poster_path"]

        backdrop = None

        if data.get("backdrop_path"):

            backdrop = IMAGE_URL + data["backdrop_path"]

        trailer = None

        videos = data.get("videos", {}).get("results", [])

        for video in videos:

            if (
                video["site"] == "YouTube"
                and video["type"] == "Trailer"
            ):

                trailer = (
                    f"https://www.youtube.com/watch?v={video['key']}"
                )

                break

        cast = []

        for actor in data.get("credits", {}).get("cast", [])[:5]:

            cast.append(actor["name"])

        return {

            "poster": poster,

            "backdrop": backdrop,

            "overview": data.get("overview"),

            "release_date": data.get("release_date"),

            "rating": data.get("vote_average"),

            "votes": data.get("vote_count"),

            "popularity": data.get("popularity"),

            "runtime": data.get("runtime"),

            "genres": [

                g["name"]

                for g in data.get("genres", [])

            ],

            "trailer": trailer,

            "cast": cast

        }

    except:

        return None