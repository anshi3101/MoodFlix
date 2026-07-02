import streamlit as st
import pandas as pd


def wishlist_page():

    st.title("❤️ My Wishlist")

    if "wishlist" not in st.session_state:

        st.session_state.wishlist = []

    wishlist = st.session_state.wishlist

    if len(wishlist) == 0:

        st.info("No movies added to wishlist yet 🍿")

        return

    movies = pd.read_pickle("movie_dict.pkl")

    movies = pd.DataFrame(movies)

    for movie in wishlist:

        row = movies[movies["title"] == movie]

        if row.empty:
            continue

        movie_id = row.iloc[0]["movie_id"]

        col1, col2 = st.columns([5,1])

        with col1:

            st.success(f"🎬 {movie}")

        with col2:

            if st.button(
                "❌",
                key=f"remove_{movie_id}"
            ):

                st.session_state.wishlist.remove(movie)

                st.rerun()

    st.markdown("---")

    if st.button(
        "🗑 Clear Wishlist",
        type="primary",
        width="stretch"
    ):

        st.session_state.wishlist = []

        st.rerun()