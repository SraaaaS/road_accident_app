# --- Add project root to Python path ---
import sys
import os
import streamlit as st
from loguru import logger

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))
    logger.info(f"ROOT_DIR added to path: {ROOT_DIR}")
# ... your existing path code
logger.info(f"ROOT_DIR added to path: {ROOT_DIR}") # <--- ADD THIS TEMPORARY LINE
from backend.models import load_best_model

from frontend.section import home, EDA_graphs, risk_prediction, about
from components.sidebar import show_sidebar


st.set_page_config(page_title="APAR" , layout="wide")

st.title("Application de Prévention des Accidents Routiers")

page = show_sidebar()

if page == "Accueil":
    home.app()
elif page == "Analyse Exploratoire des Données":
    EDA_graphs.app()
elif page == "Prediction du risque d'accident":
    best_model = load_best_model()
    risk_prediction.app(best_model)
elif page == "A propos":
    about.app()






