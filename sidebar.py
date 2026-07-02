import streamlit as st

def sidebar():

    with st.sidebar:

        # -----------------------------
        # LOGO
        # -----------------------------
        st.markdown("""
            <div style="text-align:center;padding-top:10px;">

            <div style="
            width:75px;
            height:75px;
            margin:auto;
            border-radius:50%;
            background:linear-gradient(135deg,#7C3AED,#D946EF);
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:34px;
            box-shadow:0 0 20px rgba(168,85,247,.45);
            ">
            🎬
            </div>

            <p style="
            margin-top:15px;
            font-size:13px;
            color:#B7BDD3;
            ">
            AI Movie Recommendation System
            </p>

            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # -----------------------------
        # WELCOME CARD
        # -----------------------------
        st.markdown("""
        <div style="
            background:#121826;
            padding:18px;
            border-radius:18px;
            border:1px solid #2A3048;
            text-align:center;
            margin-bottom:20px;
        ">

        <h3 style="margin-bottom:8px;">
            🍿 Welcome
        </h3>

        <p style="
            color:#B7BDD3;
            font-size:13px;
            margin-bottom:0;
        ">
        Discover movies based on your mood,
        companion and language.
        </p>

        </div>
        """, unsafe_allow_html=True)

        # -----------------------------
        # NAVIGATION
        # -----------------------------
        st.subheader("🎯 MENU")

        page = st.radio(

            "",

            [

                "🏠 Home",

                "❤️ Wishlist",

                "🕒 Recently Viewed",

                "📊 Dashboard",

                "ℹ️ About"

            ],

            label_visibility="collapsed"

        )

        st.markdown("---")

        # -----------------------------
        # QUICK STATS
        # -----------------------------
        wishlist = len(
            st.session_state.get(
                "wishlist",
                []
            )
        )

        recent = len(
            st.session_state.get(
                "recent",
                []
            )
        )

        st.subheader("📊 Quick Stats")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "❤️ Wishlist",
                wishlist
            )

        with c2:

            st.metric(
                "🕒 Recent",
                recent
            )

        st.markdown("---")

        # -----------------------------
        # INFO CARD
        # -----------------------------
        st.info(
            "💡 Tip\n\nChoose a movie, mood, companion and language to get personalized recommendations."
        )

        st.markdown("---")

        st.caption("🎬 MoodFlix v2.0")

        st.caption("Made with ❤️ using Streamlit")

    return page