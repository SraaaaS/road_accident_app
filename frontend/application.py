# --- Add project root to Python path ---
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import streamlit as st
from loguru import logger
from section import home, EDA_graphs, risk_prediction, about
from components.sidebar import show_sidebar


st.set_page_config(page_title="Application des accidents routiers" , layout="wide")
st.title("Application des accidents routiers")

page = show_sidebar()

if page == "Accueil":
    home.app()
elif page == "Analyse Exploratoire des Données":
    EDA_graphs.app()
elif page == "Prediction du risque d'accident":
    risk_prediction.app()
elif page == "A propos":
    about.app()






