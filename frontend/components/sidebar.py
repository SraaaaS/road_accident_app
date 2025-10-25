import streamlit as st

def show_sidebar():
    st.sidebar.title("Navigation")
    st.sidebar.write("Utilisez le menu pour naviguer entre les pages de l'application.")
    page = st.sidebar.radio(
        "Aller à",
        ("Accueil", "Analyse Exploratoire des Données", "Prediction du risque d'accident", 
         "A propos")
    )

    return page