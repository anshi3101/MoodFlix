import streamlit as st
import webbrowser
import urllib.parse

def format_runtime(runtime):
    try:
        runtime = int(runtime)

        h = runtime // 60
        m = runtime % 60

        if h == 0:
            return f"{m} min"

        return f"{h}h {m}m"

    except:
        return "N/A"


def display_movie(movie):

    poster = movie.get("poster")

    if not poster:
        poster = "https://via.placeholder.com/300x450?text=No+Poster"

    st.image(
        poster,
        width="stretch"
    )

    st.markdown(
        f"### {movie['title']}"
    )

    rating = movie.get("rating", "N/A")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "⭐ Rating",
            rating
        )

    with c2:
        st.metric(
            "🌍 Language",
            movie.get(
                "language",
                "NA"
            ).upper()
        )

    runtime = format_runtime(
        movie.get("runtime", 0)
    )

    st.caption(
        f"⏱ {runtime}"
    )

    genres = movie.get(
        "genres",
        []
    )

    if genres:

        gcols = st.columns(2)

        for i, genre in enumerate(genres[:4]):

            with gcols[i % 2]:
                st.success(genre)

    st.markdown("---")

    similarity = movie.get(
        "similarity",
        0
    )

    mood = movie.get(
        "mood_score",
        0
    )

    companion = movie.get(
        "companion_score",
        0
    )

    language = movie.get(
        "language_score",
        1
    )

    st.caption(
        f"🎯 Similarity {round(similarity*100)}%"
    )

    st.progress(similarity)

    st.caption(
        f"😊 Mood Match {round(mood*100)}%"
    )

    st.progress(mood)

    st.caption(
        f"👨‍👩‍👧 Companion Match {round((companion/12)*100)}%"
    )

    st.progress(
        min(
            companion/12,
            1.0
        )
    )

    st.caption(
        f"🌍 Language Match {round(language*100)}%"
    )

    st.progress(language)

    st.markdown("---")

    b1, b2 = st.columns(2)

    with b1:

        if movie.get("trailer"):

            st.link_button(
            "▶ Trailer",
            movie["trailer"],
            use_container_width=True
        )

        else:

            movie_name = urllib.parse.quote(movie["title"])

        url = (
            f"https://www.youtube.com/results?search_query="
            f"{movie_name}+official+trailer"
        )

        st.link_button(
            "▶ Trailer",
            url,
            use_container_width=True
        )

    with b2:

        if st.button(
            "❤️ Wishlist",
            key=f"wish_{movie['movie_id']}",
            width="stretch"
        ):

            if "wishlist" not in st.session_state:
                st.session_state.wishlist = []

            if movie["title"] in st.session_state.wishlist:

                st.warning("Already Added ❤️")

            else:

                st.session_state.wishlist.append(movie["title"])

                st.success("Added Successfully ❤️")

    if st.button(
        "ℹ Details",
        key=f"details_{movie['movie_id']}",
        width="stretch"
    ):

        st.session_state[
            f"show_{movie['movie_id']}"
        ] = True

    if st.session_state.get(
        f"show_{movie['movie_id']}",
        False
    ):

        with st.expander(
            "Movie Details",
            expanded=True
        ):

            st.write(
                "**Movie**",
                movie["title"]
            )

            st.write(
                "**Language**",
                movie.get(
                    "language",
                    "NA"
                ).upper()
            )

            st.write(
                "**Runtime**",
                runtime
            )

            if genres:

                st.write(
                    "**Release Date:**",
                    movie.get("release_date", "N/A")
                )

                st.write(
                    "**Rating:**",
                    movie.get("rating", "N/A")
                )

                st.write(
                    "**Votes:**",
                    movie.get("votes", "N/A")
                )

                st.write(
                    "**Popularity:**",
                    round(
                        movie.get("popularity", 0),
                        2
                    )
                )
                st.write(
                    "**Genres**",
                    ", ".join(genres)
                )

            st.write(
                "**Similarity**",
                f"{round(similarity*100)}%"
            )

            st.write(
                "**Mood Match**",
                f"{round(mood*100)}%"
            )

            st.write(
                "**Companion Match**",
                f"{round((companion/12)*100)}%"
            )

            st.write(
                "**Language Match**",
                f"{round(language*100)}%"
            )

            if movie.get("overview"):

                st.markdown("---")

                st.write(
                    movie["overview"]
                )

    if "recent" not in st.session_state:

        st.session_state.recent = []

    if movie["title"] not in st.session_state.recent:

        st.session_state.recent.append(
            movie["title"]
        )

    if len(st.session_state.recent) > 20:

        st.session_state.recent.pop(0)