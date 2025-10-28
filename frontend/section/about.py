
import streamlit as st

def app():
    st.markdown("<p style='color:#348781; font-size:34px; font-weight:bold; font-style:italic'>A propos de l'APAR...", unsafe_allow_html=True)
    st.markdown("""
    <p style='font-size:17px; color:#25383C; text-align:justify;'>
    Cette application a été développée dans le cadre de la compétition Kaggle du mois 
    d'Octobre 2025 : 
    <a href='https://www.kaggle.com/competitions/playground-series-s5e10' target='_blank' style='color:#6495ED; font-weight:bold; font-style:italic; text-decoration:none;'>
    Playground Series - Season 5, Episode 10, Predicting Road Accident Risk.
    </a>
    <br>
    Elle utilise en entrée des données sur des accidents routiers afin de prédire le risque 
    d'accident selon divers paramètres environnementaux, météorologiques et infrastructurels considérés.<br>
    Derrière cette application, des techniques avancées d'analyse de données et de machine learning
    ont été employées pour fournir les insights les plus précis et pertinents possibles aux utilisateurs.
    </p>
    <br>
    <p style='color:#438D80; font-size:18px; font-weight:bold; margin-bottom:4px;'>Objectifs de l'application :</p>
    <ul style='list-style-type:none; margin-top:0; margin-left:25px; font-size:16px; color:#25383C; padding-left:0;'>
    <li style='text-indent:-10px;'>- Analyser les tendances des accidents routiers.</li>
    <li style='text-indent:-10px;'>- Identifier les facteurs contributifs aux accidents.</li>
    <li style='text-indent:-10px;'>- Prédire le risque d'accident en fonction de divers paramètres.</li>
    </ul>
    <br>
    <p style='color:#438D80; font-size:18px; font-weight:bold; margin-bottom:4px;'>Technologies utilisées :</p>
    <ul style='list-style-type:none; margin-top:0; margin-left:25px; font-size:16px; color:#25383C;padding-left:0;'>
    <li style='text-indent:-10px;'>- <b>Streamlit</b> pour l'interface utilisateur.</li>
    <li style='text-indent:-10px;'>- <b>Pandas</b> et <b>NumPy</b> pour la manipulation des données.</li>
    <li style='text-indent:-10px;'>- <b>Scikit-learn</b> pour les modèles de machine learning.</li>
    <li style='text-indent:-10px;'>- <b>Matplotlib</b> et <b>Seaborn</b> pour la visualisation des données.</li>
    </ul>
    <br>
    <p style='font-size:16px; color:#25383C;'>
    <span style='color:#438D80; font-weight:bold;'>Application développée par :</span>  
    <a href='https://github.com/SraaaaS' target='_blank' style='color:#6495ED; font-weight:bold; font-style:italic; text-decoration:none;'>
    SraaaaS</a>
    <br><br>
    <span style='color:#438D80; font-weight:bold;'>Date :</span> Octobre 2025
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <hr style='margin-top:40px; margin-bottom:20px;'>

    <div style='display:flex; justify-content:center; align-items:center; gap:25px; flex-wrap:wrap;'>
    <img src='https://streamlit.io/images/brand/streamlit-mark-color.png' width='50' title='Streamlit'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg' width='90' title='Pandas'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/1/1a/NumPy_logo.svg' width='80' title='NumPy'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg' width='90' title='Scikit-learn'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg' width='85' title='Matplotlib'>
    <img src='https://seaborn.pydata.org/_static/logo-wide-lightbg.svg' width='100' title='Seaborn'>
    </div>

    <p style='text-align:center; font-size:14px; color:#25383C; margin-top:10px;'>
    Outils utilisés pour le développement de l'application
    </p>
    """, unsafe_allow_html=True)
