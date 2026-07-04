import ast
import pickle
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
    initial_sidebar_state="auto"
)

st.markdown("""
<style>

.block-container{
    padding-top:0.2rem !important;
    padding-bottom:1rem !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

header{
    background:transparent !important;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

[data-testid="stDecoration"]{
    display:none;
}

[data-testid="stStatusWidget"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)



def load_css():

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


@st.cache_resource
def load_movies():

    movies_dict = pickle.load(
        open("movie_dict.pkl", "rb")
    )

    movies = pd.DataFrame(movies_dict)

    tmdb = pd.read_csv(
        "tmdb_5000_movies.csv"
    )

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

    similarity = pickle.load(

        open("similarity.pkl", "rb")

    )

    return movies, similarity


movies, similarity = load_movies()



@st.cache_data(show_spinner=False)
def get_recommendations(movie,mood,companion,language):

    return pipeline_recommend(
        movie,
        mood,
        companion,
        language,
        top_n=5
    )



page = sidebar()

# Store recommendations between reruns
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []


st.markdown("""

<div class="hero-header">

<div>

<h1 id="moodflix-title">

🎬 Mood<span>Flix</span>

</h1>

<div class="hero-tagline">

✨ Personalized • AI Powered • Mood Based Recommendations

</div>

<div class="hero-desc">

Find your next favourite movie using AI,
your mood, your companion and preferred language.

</div>

</div>

<div class="hero-badge">

🍿 Version 2.0

</div>

</div>

""", unsafe_allow_html=True)

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

recommend_btn = st.button(
    "🎬 Get Recommendations",
    type="primary",
    width="stretch"
)


if recommend_btn:

    with st.spinner("🎬 Finding Perfect Movies For You..."):

        st.session_state.recommendations = get_recommendations(
            selected_movie_name,
            selected_mood,
            selected_companion,
            selected_language
        )

        st.success(
            f"🍿 Found {len(st.session_state.recommendations)} recommendations for you!"
        )

recommendations = st.session_state.recommendations

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
💜 Recommended For You
</div>
""", unsafe_allow_html=True)

if len(recommendations) == 0:

    st.warning(
        "😔 No movies found."
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