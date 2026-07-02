MOOD_GENRES = {

    "Happy": [
        "Comedy",
        "Animation",
        "Family",
        "Music"
    ],

    "Relaxed": [
        "Documentary",
        "Fantasy",
        "Family",
        "TVMovie"
    ],

    "Excited": [
        "Action",
        "Adventure",
        "ScienceFiction"
    ],

    "Thrilling": [
        "Thriller",
        "Mystery",
        "Crime",
        "Horror"
    ],

    "Romantic": [
        "Romance",
        "Drama"
    ],

    "Motivated": [
        "History",
        "War",
        "Adventure"
    ],

    "Exploring": [
        "Western",
        "Foreign",
        "Fantasy",
        "Adventure"
    ]
}
def get_mood_score(movie_genres,mood):
    
    if mood not in MOOD_GENRES:
        return 0
    
    mood_genres = MOOD_GENRES[mood]
    score = 0
    
    for genre in movie_genres:
        
        if genre in mood_genres:
            score += 1
            
    normalized_score = score / len(mood_genres)
    return normalized_score

def mood_filter(content_movies, mood, top_n=30):

    """
    Re-rank content-based recommendations according to user's mood.
    """

    filtered_movies = []

    for movie in content_movies:

        if "genres" not in movie:
            continue

        mood_score = get_mood_score(
            movie["genres"],
            mood
        )

        movie["mood_score"] = mood_score

        filtered_movies.append(movie)

    filtered_movies.sort(

        key=lambda x: (
            x["mood_score"],
            x["similarity"]
        ),

        reverse=True
    )

    return filtered_movies[:top_n]
