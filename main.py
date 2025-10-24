import streamlit as st
import joblib
from loguru import logger



joblib.load("model/GradientBoosting.pkl")

logger.info("Démarrage de l'application Streamlit")



st.set_page_config(page_title="Accident Risk Prediction" , layout="wide")
st.title("Accident Risk Prediction Application")


