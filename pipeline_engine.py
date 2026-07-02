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
    content_movies = recommend(movie, top_n=300)
    
    mood_movies = mood_filter(
        content_movies,
        mood,
        top_n=30
    )
    
    companion_movies = companion_filter(
        mood_movies,
        companion,
        top_n=15
    )
    
    final_movies = language_filter(
        companion_movies,
        preferred_language,
        top_n=top_n
    )
    
    return final_movies