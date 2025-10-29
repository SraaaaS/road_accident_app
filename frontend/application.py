import sys
import os
import streamlit as st
from loguru import logger

st.set_page_config(
    page_title="Application de Prévention contre les Accidents Routiers", 
    layout="wide", page_icon="🚘" 
)

image_url = "https://raw.githubusercontent.com/SraaaaS/road_accident_app/master/APAR_thumbnail.png" 

og_image_tag = f"""
    <meta property="og:image" content="{image_url}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
"""

st.components.v1.html(og_image_tag, height=0, width=0)

if "path_added" not in st.session_state:
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if str(ROOT_DIR) not in sys.path:
        sys.path.append(str(ROOT_DIR))
        logger.info(f"ROOT_DIR added to path: {ROOT_DIR}")
    st.session_state["path_added"] = True
 
from backend.models import load_best_model

from frontend.section import home, EDA_graphs, risk_prediction, about
from components.sidebar import show_sidebar


#st.set_page_config(page_title="APAR" , layout="wide")

st.markdown("""
<p style='color:#25383C; font-size:40px; font-weight:bold; margin-top:0; margin-bottom:10px;'>
  <span style='color:#438D80; font-size:44px;'>A</span>pplication de 
  <span style='color:#438D80; font-size:44px;'>P</span>révention des 
  <span style='color:#438D80; font-size:44px;'>A</span>ccidents 
  <span style='color:#438D80; font-size:44px;'>R</span>outiers
</p>
""", unsafe_allow_html=True)
st.write("---") 

page = show_sidebar()

if page == "Accueil":
    home.app()
elif page == "Analyse Exploratoire des Données":
    EDA_graphs.app()
elif page == "Prédiction du risque d'accident":
    best_model = load_best_model()
    risk_prediction.app(best_model)
elif page == "A propos de l'APAR...":
    about.app()






