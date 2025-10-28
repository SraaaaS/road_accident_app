import streamlit as st
from loguru import logger
import pandas as pd
import joblib
from frontend.components.forms import risk_form
from backend.preprocessing import feature_engineering
from backend.models import predict, load_best_model

def app(best_model):
    st.markdown("<p style='color:#348781; font-size:34px; font-weight:bold'>Prediction du risque d'accident", unsafe_allow_html=True)
    
    #Load model
    try:
        model = joblib.load("model/best_model.pkl")
        st.info("Modèle chargé avec succès. Prêt pour la prédiction.")
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {e}")
        return
    
    #user input
    user_input = risk_form()
    if user_input is not None:
        input_df = pd.DataFrame([user_input])
        input_processed = feature_engineering(input_df)
        #Prediction
        try:
            expected_features = best_model.feature_names_
            # Réordonner et s'assurer que toutes les colonnes sont présentes
            input_processed = input_processed.reindex(columns=expected_features, fill_value=0)

            prediction = predict(best_model, input_processed)[0]
            st.success("**Resultat de la prediction :**")
            st.metric(label="Dans ces conditions, le risque que le conducteur soit impliqué dans un accident est de :", value=f"{100*prediction:.2f} %")
        except Exception as e:
            st.error(f"Erreur lors de la prediction : {e}")


