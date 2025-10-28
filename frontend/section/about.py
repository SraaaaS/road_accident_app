
import streamlit as st

def app():
    st.markdown("<p style='color:#348781; font-size:42px; font-weight:bold'>A propos de cette application...", unsafe_allow_html=True)
    st.markdown("""
    Cette application a été développée dans le cadre de la compétition Kaggle du mois 
    d'Octobre 2025 : ***"Playground Series - Season 5, Episode 10, Predicting Road Accident Risk"***
    Elle utilise en entrée des données sur des accidents routiers de sorte à predire le risque 
    d'accident selon les divers parametres environnementaux, meteorologiques et infrastrcuturels 
    considérés. 
    Derriere cette application des techniques avancées d'analyse de données et de machine learning
    ont été emloyées pour fournir des insights les plus precises et pertinentes possibles aux utilisateurs.
             
    **:#438D80[Objectifs de l'application :]**
    
        -Analyser les tendances des accidents routiers.
             
        -Identifier les facteurs contributifs aux accidents.
             
        -Prédire le risque d'accident en fonction de divers paramètres.
             
    
    **:#438D80[Technologies utilisées :]**
             
        -Streamlit pour l'interface utilisateur.
             
        -Pandas et NumPy pour la manipulation des données.
             
        -Scikit-learn pour les modèles de machine learning.
             
        -Matplotlib et Seaborn pour la visualisation des données.
             
             
    **:#438D80[Application développée par :]** Sara
             
    **:#438D80[Date :]** Octobre 2025
             
""")
