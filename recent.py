import streamlit as st


def recent_page():

    st.title("🕒 Recently Viewed")

    if "recent" not in st.session_state:

        st.session_state.recent = []

    if len(st.session_state.recent) == 0:

        st.info("No recently viewed movies.")

        return

    for movie in reversed(st.session_state.recent):

        st.success(f"🎬 {movie}")

    st.markdown("---")

    if st.button(
        "🗑 Clear History",
        width="stretch"
    ):

        st.session_state.recent = []

        st.rerun()