import streamlit as st
import pandas as pd


def dashboard(movies):

    st.title("📊 MoodFlix Analytics Dashboard")

    total_movies = len(movies)

    total_languages = movies["original_language"].nunique()

    total_runtime = int(
        movies["runtime"].fillna(0).mean()
    )

    wishlist_count = len(
        st.session_state.get(
            "wishlist",
            []
        )
    )

    genre_set = set()

    for genres in movies["genres"]:

        if isinstance(genres, list):

            for g in genres:
                genre_set.add(g)

    total_genres = len(genre_set)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🎬 Movies",
        total_movies
    )

    c2.metric(
        "🎭 Genres",
        total_genres
    )

    c3.metric(
        "🌍 Languages",
        total_languages
    )

    c4.metric(
        "❤️ Wishlist",
        wishlist_count
    )

    st.markdown("---")

    c5, c6 = st.columns(2)

    c5.metric(
        "⏱ Avg Runtime",
        f"{total_runtime} min"
    )

    c6.metric(
        "⭐ Avg Rating",
        round(
            movies["vote_average"].fillna(0).mean(),
            2
        )
    )

    st.markdown("---")

    st.subheader("🌍 Language Distribution")

    lang = (
        movies["original_language"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(lang)

    st.markdown("---")

    st.subheader("⏱ Runtime Distribution")

    runtime = (
        movies["runtime"]
        .dropna()
    )

    st.area_chart(runtime)

    st.success(
        "Dashboard Updated Successfully 🚀"
    )