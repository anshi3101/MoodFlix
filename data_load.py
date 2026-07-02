import pickle
import pandas as pd

# -----------------------------
# Load movie dictionary
# -----------------------------
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

# -----------------------------
# Load enriched movie details
# -----------------------------
enriched = pickle.load(open("movies_enriched.pkl", "rb"))
enriched = pd.DataFrame(enriched)

# Remove duplicate movie_ids if any
enriched.drop_duplicates(subset="movie_id", inplace=True)

# Make movie_id the index for O(1) lookup
enriched.set_index("movie_id", inplace=True)


def get_movie(movie_id):
    """
    Returns movie details using movie_id.
    Very fast lookup because movie_id is the DataFrame index.
    """

    try:
        return enriched.loc[movie_id]
    except KeyError:
        return None