import streamlit as st

st.title("Roteiro 1: Primeiros Passos com Streamlit")

texto = st.text_input('digite alguma coisa! :)')
if st.button("Clique-me"):
    st.write(texto)
