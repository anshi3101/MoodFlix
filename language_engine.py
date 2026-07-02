LANGUAGES_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Bengali": "bn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Korean": "ko",
    "Japanese": "ja",
    "Chinese": "zh",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Russian": "ru",
    "Arabic": "ar"
}


def get_language_score(movie_language, preferred_language):

    """
    Returns:
        1 -> Language matches
        0 -> Language doesn't match
    """

    if preferred_language not in LANGUAGES_CODES:
        return 0

    preferred_code = LANGUAGES_CODES[preferred_language]

    if movie_language == preferred_code:
        return 1

    return 0


def language_filter(content_movies, preferred_language, top_n=10):

    """
    Re-rank movies according to preferred language.
    """

    if preferred_language not in LANGUAGES_CODES:
        return content_movies[:top_n]

    matched_movies = []
    unmatched_movies = []

    for movie in content_movies:

        language_score = get_language_score(
            movie.get("language", ""),
            preferred_language
        )

        movie["language_score"] = language_score

        if language_score == 1:
            matched_movies.append(movie)
        else:
            unmatched_movies.append(movie)

    if len(matched_movies) >= top_n:

        return matched_movies[:top_n]

    remaining = top_n - len(matched_movies)

    return matched_movies + unmatched_movies[:remaining]