import streamlit as st
from loguru import logger
import pandas as pd
import joblib
from frontend.components.forms import risk_form
from backend.preprocessing import feature_engineering
from backend.models import predict, load_best_model

def app(best_model):
    st.title("Prediction du risque d'accident")

    # #Load model
    # try:
    #     model = joblib.load("model/best_model.pkl")
    #     st.success("Modèle chargé avec succès.")
    # except Exception as e:
    #     st.error(f"Erreur lors du chargement du modèle : {e}")
    #     return
    
    #user input
    user_input = risk_form()
    if user_input is not None:
        input_df = pd.DataFrame([user_input])
        input_processed = feature_engineering(input_df)
        #Prediction
        try:
            prediction = predict(best_model, input_processed)
            st.success(f"Resultat de la prediction : {prediction}")
        except Exception as e:
            st.error(f"Erreur lors de la prediction : {e}")

