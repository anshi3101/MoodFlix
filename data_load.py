import pickle
import pandas as pd


movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)


enriched = pickle.load(open("movies_enriched.pkl", "rb"))
enriched = pd.DataFrame(enriched)


enriched.drop_duplicates(subset="movie_id", inplace=True)


enriched.set_index("movie_id", inplace=True)


def get_movie(movie_id):

    #Returns movie details using movie_id.


    try:
        return enriched.loc[movie_id]
    except KeyError:
        return None