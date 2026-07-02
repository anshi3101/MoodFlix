from content_based import recommend
from mood_engine import mood_filter
from companion_engine import companion_filter
from language_engine import language_filter


def pipeline_recommend(
    movie,
    mood,
    companion,
    preferred_language,
    top_n=5
):
    """
    Complete Recommendation Pipeline

    Step 1 -> Content Based Recommendation
    Step 2 -> Mood Filtering
    Step 3 -> Companion Filtering
    Step 4 -> Language Filtering

    Returns:
        List of Final Recommended Movies
    """

    # -----------------------------------
    # Step 1 : Content Based Recommendation
    # -----------------------------------

    content_movies = recommend(
        movie=movie,
        top_n=50
    )

    if not content_movies:
        return []

    # -----------------------------------
    # Step 2 : Mood Filter
    # -----------------------------------

    mood_movies = mood_filter(
        content_movies=content_movies,
        mood=mood,
        top_n=25
    )

    if not mood_movies:
        mood_movies = content_movies

    # -----------------------------------
    # Step 3 : Companion Filter
    # -----------------------------------

    companion_movies = companion_filter(
        mood_movies,
        companion,
        top_n=15
    )

    if not companion_movies:
        companion_movies = mood_movies

    # -----------------------------------
    # Step 4 : Language Filter
    # -----------------------------------

    final_movies = language_filter(
        companion_movies,
        preferred_language,
        top_n=top_n
    )

    if not final_movies:
        final_movies = companion_movies[:top_n]

    return final_movies