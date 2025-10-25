
import streamlit as st

def app():
    st.title("A propos de cette application")
    st.write("""
    Cette application a été développée dans le cadre de la compétition Kaggle du mois 
    d'Octobre 2025 : "Playground Series - Season 5, Episode 10, Predicting Road Accident Risk"
    Elle utilise en entrée des données sur des accidents routiers de sorte à predire le risque 
    d'accident selon les divers parametres environnementaux, meteorologiques et infrastrcuturels 
    considérés. 
    Derriere cette application des techniques avancées d'analyse de données et de machine learning
    ont été emloyées pour fournir des insights les plus precises et pertinentes possibles aux utilisateurs.
             
    Objectifs de l'application :
        - Analyser les tendances des accidents routiers.
             
        - Identifier les facteurs contributifs aux accidents.
             
        - Prédire le risque d'accident en fonction de divers paramètres.
             
    
    Technologies utilisées :
             
        - Streamlit pour l'interface utilisateur.
             
        - Pandas et NumPy pour la manipulation des données.
             
        - Scikit-learn pour les modèles de machine learning.
             
        - Matplotlib et Seaborn pour la visualisation des données.
             
             
    Application développé par : Sara
             
    Date : Octobre 2025
             
""")
