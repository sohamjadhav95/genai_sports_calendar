import streamlit as st
import requests

st.set_page_config(page_title="GenAI Sports Tournament Calendar", layout="wide")
st.title("🏆 GenAI Sports Tournament Calendar")

API_URL = "http://127.0.0.1:8000/tournaments"
REFRESH_URL = "http://127.0.0.1:8000/refresh"

if st.button("🔄 Refresh Tournaments (Scrape + Extract)"):
    with st.spinner("Refreshing tournaments..."):
        resp = requests.post(REFRESH_URL)
        if resp.status_code == 200:
            st.success("Tournaments refreshed!")
        else:
            st.error(f"Refresh failed: {resp.text}")

st.markdown("---")

try:
    resp = requests.get(API_URL)
    tournaments = resp.json()
except Exception as e:
    st.error(f"Error fetching tournaments: {e}")
    tournaments = []

if tournaments:
    for t in tournaments:
        with st.container():
            st.subheader(t['name'])
            cols = st.columns([2, 2, 2, 6])
            cols[0].markdown(f"**Level:** {t['level']}")
            cols[1].markdown(f"**Dates:** {t['start_date']} - {t['end_date']}")
            cols[2].markdown(f"**URL:** [Event Link]({t['url']})" if t['url'] else "")
            if t['image_url'] and t['image_url'] != "N/A":
                cols[3].image(t['image_url'], width=180)
            st.markdown(f"**Streaming:** {' | '.join(t['streaming_links']) if t['streaming_links'] else 'N/A'}")
            st.markdown(f"**Summary:** {t['summary']}")
            st.markdown("---")
else:
    st.info("No tournaments found. Click 'Refresh' to load data.")
