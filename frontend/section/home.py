import streamlit as st

def app():
    st.title("Bienvenue sur la page d'accueil de l'application Road Accident Analysis")
    st.write("""Cette application vise à analyser les données des accidents de la route 
             pour identifier les tendances et les facteurs contributifs.
             
             Vous pouvez naviguer à travers les différentes sections de l'application 
             pour explorer les données, visualiser les analyses et obtenir des insights 
             précieux.
             
             Utilisez le menu de navigation sur le côté pour accéder aux différentes fonctionnalités.""")
    st.image("frontend/components/home_pic.png", use_column_width=True)
    
