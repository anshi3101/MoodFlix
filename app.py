import os
import pickle
import gdown
import pandas as pd
import streamlit as st

from pipeline_engine import pipeline_recommend
from mood_engine import MOOD_GENRES
from genre_profiles import COMPANION_GENRES
from language_engine import LANGUAGES_CODES

from sidebar import sidebar
from dashboard import dashboard
from wishlist import wishlist_page
from movie_card import display_movie
from recent import recent_page

st.set_page_config(
    page_title="MoodFlix",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

page = sidebar()


st.markdown("""
    <h1 style='margin-bottom:5px;font-size:48px;font-weight:700;'>
    🎬 Mood<span style="color:#A855F7;">Flix</span>
    </h1>

    <p style="color:#9CA3AF;font-size:15px;margin-top:-8px;">
    AI Powered Movie Recommendation System
    </p>
    """, unsafe_allow_html=True)

FILE_ID = "1qpAcZ56oo14B1qbeuDJN893N4wKVlnuL"

if not os.path.exists("similarity.pkl"):
    gdown.download(
        f"https://drive.google.com/uc?id={FILE_ID}",
        "similarity.pkl",
        quiet=False
    )
    
movies_dict = pickle.load(open('movie_dict.pkl','rb'))

movies = pd.DataFrame(movies_dict)

import ast

tmdb = pd.read_csv("tmdb_5000_movies.csv")


def extract(x):

    try:
        return [
            i["name"]
            for i in ast.literal_eval(x)
        ]

    except:
        return []


tmdb["genres"] = tmdb["genres"].apply(extract)

movies = movies.merge(

    tmdb[

        [

            "title",

            "genres",

            "runtime",

            "vote_average",

            "original_language"

        ]

    ],

    on="title",

    how="left"

)

if page == "🕒 Recently Viewed":

    recent_page()

    st.stop()

if page == "📊 Dashboard":

    dashboard(movies)

    st.stop()

elif page == "❤️ Wishlist":

    wishlist_page()

    st.stop()

elif page == "ℹ️ About":

    st.title("About MoodFlix")

    st.write("""
MoodFlix is an AI Powered Movie Recommendation System.

Recommendation is based on:

• Content Similarity

• Mood

• Companion

• Preferred Language
""")

    st.stop()
    
similarity = pickle.load(open('similarity.pkl','rb'))

st.markdown("<br>",unsafe_allow_html=True)

st.markdown("""
<div class="glass fade">

<div class="hero-container">
            
<div class="hero-left">

<div class="hero-title">

Your Next Watch <br>

Is Here 🍿

</div>

<div class="hero-sub">

Smart recommendations based on your mood,
companion and preferred language.

</div>

</div>

<div>

<img
src="https://images.unsplash.com/photo-1534447677768-be436bb09401?w=900"
style="
width:100%;
max-width:420px;
border-radius:18px;
">

</div>

</div>

</div>

""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='glass'>
<h3 style="margin-top:0px;">
💜 Tell us about yourself
</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([2.3,1.5,1.7,1.7,1.2])

with col1:

    selected_movie_name = st.selectbox(
        "🎥 Choose a Movie",
        movies["title"].values
    )

with col2:

    selected_mood = st.selectbox(
        "😊 Mood",
        list(MOOD_GENRES.keys())
    )

with col3:

    selected_companion = st.selectbox(
        "👨‍👩‍👧 Companion",
        list(COMPANION_GENRES.keys())
    )

with col4:

    selected_language = st.selectbox(
        "🌍 Language",
        list(LANGUAGES_CODES.keys())
    )

with col5:

    st.write("")
st.write("")

recommend_btn = st.button(
    "🎬 Get Recommendations",
    type="primary",
    width="stretch"
)


if recommend_btn:

    with st.spinner(
        "🎬 Finding Perfect Movies For You..."
    ):

        recommendations = pipeline_recommend(
            movie=selected_movie_name,
            mood=selected_mood,
            companion=selected_companion,
            preferred_language=selected_language,
            top_n=5
        )

        st.success(
            f"🍿 Found {len(recommendations)} recommendations for you!"
        )
    #st.write(recommendations)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
    💜 Recommended For You
    </div>
    """, unsafe_allow_html=True)

    if len(recommendations) == 0:

        st.warning(
            "😔 No movies found. Try another mood or language."
        )

    else:

        cols = st.columns(len(recommendations))

        for i, movie in enumerate(recommendations):

            with cols[i]:

                with st.container(border=True):

                    display_movie(movie)

st.markdown("---")

st.caption(
    "🎬 MoodFlix • AI Powered Movie Recommendation System"
)

st.caption(
    "Built with Streamlit • TMDB Dataset • Content-Based + Mood + Companion + Language Recommendation"
)