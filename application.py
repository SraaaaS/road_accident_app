import streamlit as st
import joblib

joblib.load("model/best_model.pkl")

st.set_page_config(page_title="Accident Risk Prediction" , layout="wide")
