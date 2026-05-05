import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-rec-466x.onrender.com"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="Movie Recommender", layout="wide")

# =============================
# CSS
# =============================
st.markdown("""
<style>


/* SEARCH */
input {
    border-radius: 12px !important;
    height: 50px !important;
}

/* CATEGORY */
.stRadio > div {
    flex-direction: row;
    gap: 10px;
}


/* CARD */
.movie-title {
    font-size: 0.85rem;
    text-align: center;
    margin-top: 6px;
}

/* BUTTON */
.stButton button {
    width: 100%;
    border-radius: 8px;
}

/* FOOTER */
.footer {
    text-align: center;
    margin-top: 40px;
    color: #6b7280;
}
</style>
""", unsafe_allow_html=True)

# =============================
# STATE
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"

if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

# =============================
# NAVIGATION
# =============================
def goto_home():
    st.session_state.view = "home"
    st.session_state.selected_tmdb_id = None
    st.rerun()

def goto_details(tmdb_id):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = tmdb_id
    st.rerun()

# =============================
# API
# =============================
@st.cache_data(ttl=60)
def api_get(path, params=None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params)
        return r.json()
    except:
        return None

# =============================
# GRID
# =============================
def poster_grid(cards, cols=5):
    if not cards:
        st.info("No movies found.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0

    for _ in range(rows):
        colset = st.columns(cols)

        for col in colset:
            if idx >= len(cards):
                break

            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Unknown")
            poster = m.get("poster_url")

            with col:
                if poster:
                    st.image(poster, use_container_width=True)
                else:
                    st.write("No Image")

                if st.button("Open", key=f"open_{tmdb_id}_{idx}"):
                    goto_details(tmdb_id)

                st.markdown(
                    f"<div class='movie-title'>{title}</div>",
                    unsafe_allow_html=True
                )

# =============================
# TOP BAR
# =============================
col1, col2 = st.columns([1.5,5.5])

with col2:
    st.title("Movie Recommendation System")

with col1:
    if st.button("Home"):
        goto_home()

# =============================
# HOME
# =============================
if st.session_state.view == "home":

    query = st.text_input("", placeholder="Search movies (Avengers, Batman...)")

    category = st.radio(
        "",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        horizontal=True
    )

    st.divider()

    # SEARCH
    if query:
        data = api_get("/tmdb/search", {"query": query})
        cards = []

        if data and "results" in data:
            for m in data["results"][:24]:
                cards.append({
                    "tmdb_id": m.get("id"),
                    "title": m.get("title", "Unknown"),
                    "poster_url": f"{TMDB_IMG}{m.get('poster_path')}" if m.get("poster_path") else None
                })

        st.markdown("### Results")
        poster_grid(cards)

    else:
        data = api_get("/home", {"category": category})
        if data:
            poster_grid(data)

# =============================
# DETAILS
# =============================
elif st.session_state.view == "details":

    tmdb_id = st.session_state.selected_tmdb_id
    data = api_get(f"/movie/id/{tmdb_id}")

    if not data:
        st.error("Failed to load movie")
        if st.button("Back"):
            goto_home()

    else:
        title = data.get("title", "Unknown Title")
        release = data.get("release_date", "N/A")
        genres = ", ".join([g["name"] for g in data.get("genres", [])])

        if data.get("backdrop_url"):
            st.image(data["backdrop_url"], use_container_width=True)

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(data.get("poster_url"), use_container_width=True)

        with col2:
            st.markdown(f"## {title}")
            st.markdown(f"**Release:** {release}")
            st.markdown(f"**Genres:** {genres}")
            st.write(data.get("overview", "No overview available."))

        st.divider()

        st.markdown("### Recommendations")

        bundle = api_get("/movie/search", {"query": title})

        if bundle:
            st.markdown("#### Similar Movies")

            tfidf_cards = []
            for x in bundle.get("tfidf_recommendations", []):
                if x.get("tmdb"):
                    tfidf_cards.append({
                        "tmdb_id": x["tmdb"].get("tmdb_id"),
                        "title": x["tmdb"].get("title", "Unknown"),
                        "poster_url": x["tmdb"].get("poster_url")
                    })

            poster_grid(tfidf_cards)

            st.markdown("#### More Like This")
            poster_grid(bundle.get("genre_recommendations", []))

# =============================
# FOOTER
# =============================
st.markdown("""
<div class="footer">
Movie Recommendation System
</div>
""", unsafe_allow_html=True)