import streamlit as st
import pandas as pd


def wishlist_page():

    st.title("❤️ My Wishlist")

    if "wishlist" not in st.session_state:
        st.session_state.wishlist = []

    wishlist = st.session_state.wishlist

    if len(wishlist) == 0:

        st.info("🍿 Your wishlist is empty.")

        return

    movies = pd.read_pickle("movie_dict.pkl")
    movies = pd.DataFrame(movies)

    for movie in wishlist:

        row = movies[movies["title"] == movie]

        if row.empty:
            continue

        movie_id = row.iloc[0]["movie_id"]

        # Card
        with st.container(border=True):

            col1, col2 = st.columns([10, 1], gap="small")

            with col1:

                st.markdown(f"### 🎬 {movie}")

            with col2:

                if st.button(
                    "🗑️",
                    key=f"remove_{movie_id}",
                    use_container_width=True
                ):

                    st.session_state.wishlist.remove(movie)

                    st.toast(
                        "Removed from Wishlist ❤️",
                        icon="🗑️"
                    )

                    st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "🗑 Clear Wishlist",
        type="primary",
        use_container_width=True
    ):

        st.session_state.wishlist = []

        st.toast(
            "Wishlist Cleared",
            icon="🗑️"
        )

        st.rerun()