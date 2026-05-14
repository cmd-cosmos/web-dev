#pylint: skip-file
#type: ignore

import streamlit as st

st.title("Title")
st.header("Header")
st.subheader("Subheader")

st.text_input(label="Input Box", placeholder="input box")

st.columns(2)

if st.button("button") and not st.button("reset"):
    st.warning("WARNING")