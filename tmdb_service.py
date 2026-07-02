import requests
from functools import lru_cache
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

API_KEY = "32f8ac1a21f52f177d724040cdf7a57d"

BASE_URL = "https://api.themoviedb.org/3"

IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# -----------------------------
# Reusable Session
# -----------------------------

session = requests.Session()

retry = Retry(
    total=5,
    connect=5,
    read=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(
    max_retries=retry,
    pool_connections=20,
    pool_maxsize=20
)

session.mount("https://", adapter)
session.mount("http://", adapter)

session.headers.update({
    "User-Agent": "MoodFlix/1.0"
})

# -----------------------------
# Fetch Movie Details
# -----------------------------

@lru_cache(maxsize=5000)
def fetch_movie_details(movie_id):

    url = f"{BASE_URL}/movie/{movie_id}"

    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "append_to_response": "videos,credits"
    }

    try:

        # Prevent Rate Limit
        time.sleep(0.15)

        response = session.get(
            url,
            params=params,
            timeout=20
        )

        if response.status_code != 200:
            print(f"TMDB Error {response.status_code} : {movie_id}")
            return None

        data = response.json()

        poster = None
        if data.get("poster_path"):
            poster = IMAGE_URL + data["poster_path"]

        backdrop = None
        if data.get("backdrop_path"):
            backdrop = IMAGE_URL + data["backdrop_path"]

        trailer = None

        for video in data.get("videos", {}).get("results", []):

            if (
                video.get("site") == "YouTube"
                and video.get("type") == "Trailer"
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

    except Exception as e:

        print("TMDB Exception :", e)

        return None