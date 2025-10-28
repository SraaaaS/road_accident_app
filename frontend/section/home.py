import streamlit as st

def app():
    st.markdown("<p style='color:#348781; font-size:42px; font-weight:bold'>Bienvenue sur la page d'accueil de l'application Road Accident Analysis", unsafe_allow_html=True)
    st.image("frontend/components/home_pic.png", use_column_width=True)
    st.write("""Cette application vise à analyser les données des accidents de la route pour identifier les **tendances** et les **facteurs contributifs**.
              Vous pouvez naviguer à travers les différentes sections de l'application pour **explorer les données**, **visualiser les analyses** et obtenir des **insights** précieux.
             Utilisez le **menu de navigation** sur le côté pour accéder aux différentes fonctionnalités.""")
    
    
