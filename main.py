import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content
)

st.title("AI Scraper Web")
ur = st.text_input("Enter URL")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(ur)

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View Content"):
        st.text_area("Dom Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Enter Description")
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)