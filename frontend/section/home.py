import streamlit as st

def app():
    st.markdown("<p style='color:#348781; font-size:34px; font-weight:bold'>Bienvenue sur la page d'accueil de l'APAR* !", unsafe_allow_html=True)
    st.write("""Cette application vise à analyser les données des accidents de la route pour identifier les **tendances** et les **facteurs contributifs**.
            \nVous pouvez naviguer à travers les différentes sections de l'application pour **explorer les données**, **visualiser les analyses** et obtenir des **insights** précieux.
             \nUtilisez le **menu de navigation** sur le côté pour accéder aux différentes fonctionnalités.""")
    st.image("frontend/components/home_pic.png", use_column_width=True)
    st.caption("Image illustrative de la competition <span style='font-style:italic'>Playground Series - Season 5, Episode 10</span> sur Kaggle", unsafe_allow_html=True )
    st.caption("\n*APAR = Application de Prévention contre les Accidents Routiers")
    
