import streamlit as st
from scrape import scrape_website

st.title("AI Scraper Web")
ur = st.text_input("Enter URL")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(ur)