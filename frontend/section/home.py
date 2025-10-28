import streamlit as st

def app():
    st.markdown("""<p style='color:#348781; font-size:34px; font-weight:bold'>🚘Vous êtes bien sur la page d'accueil de l'APAR* !""", 
                unsafe_allow_html=True)
    st.markdown("""Cette application vise à analyser les données des accidents de la route de sorte à en tirer les **tendances** et les **facteurs contributifs** permettant de réaliser les prévisions de ce risque dans diverses situation recontextualisées.
            \nVous pouvez naviguer à travers les différentes sections de l'application pour **explorer les données**, **visualiser les analyses** et obtenir des **insights** précieux.
             \nUtilisez le **menu de navigation** sur le côté pour accéder aux différentes fonctionnalités.""")
    st.image("frontend/components/home_pic.png", use_column_width=True)
    st.caption("Image illustrative de la competition <span style='font-style:italic'>Playground Series - Season 5, Episode 10</span> sur Kaggle", unsafe_allow_html=True )
    st.caption("\n*APAR = Application de Prévention contre les Accidents Routiers")
    
