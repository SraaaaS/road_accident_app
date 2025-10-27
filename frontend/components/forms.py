import streamlit as st
import pandas as pd

def risk_form():
    with st.form(key='risk_form'):
        st.write("Veuillez entrer les paramètres pour prédire le risque d'accident :")

        st.subheader("Conditions routières:")

        road_type = st.selectbox("Type de route", 
                                ["Autoroute", "Route de Ville", "Route de campagne"])
        lighting = st.selectbox("Conditions d'éclairage",
                                  ["Lumiere du soleil", "Eclairage Nocturne", "Sombre"])
        weather = st.selectbox("Conditions météorologiques",
                               ["Pluvieux", "Brouillard", "Eclairci"])
        time_of_day = st.selectbox("Moment de la journée",
                                   ["Matin", "Après-midi", "Soir"])
        curvature = st.slider("Courbure de la route", 0, 90, 10)
        num_lanes = st.slider("Nombre de voies", 1, 5, 1)
        speed_limit = st.slider("Limite de vitesse", 20, 130, 10)
        road_sign_present = st.toggle("Présence de panneaux de signalisation", True)
        public_road = st.toggle("Route publique", True)
        holiday = st.toggle("Jour férié", False)
        school_season = st.toggle("Saison scolaire", True)
        num_reported_accidents = st.selectbox("Nombre d'accidents signalés dans la zone", options=list(range(5)), index=1)

                                         
        submitted = st.form_submit_button('Prédire le risque d\'accident')
        if submitted==True:
            st.success("Données entrées avec succès! Préparation de la prédiction...")
            # 🎯 MAPPING des valeurs françaises vers les labels du modèle
            road_type_map = {
                "Autoroute": "highway",
                "Route de Ville": "urban",
                "Route de campagne": "rural"
            }
            lighting_map = {
                "Lumiere du soleil": "daylight",
                "Eclairage Nocturne": "night",
                "Sombre": "dim"
            }
            weather_map = {
                "Eclairci": "clear",
                "Brouillard": "foggy",
                "Pluvieux": "rainy"
            }
            time_of_day_map = {
                "Matin": "morning",
                "Après-midi": "afternoon",
                "Soir": "evening"
            }

            # Appliquer les mappings
            return {
                "id": 0,
                "road_type": road_type_map[road_type],
                "num_lanes": num_lanes,
                "curvature": curvature,
                "speed_limit": speed_limit,
                "lighting": lighting_map[lighting],
                "weather": weather_map[weather],
                "road_signs_present": road_sign_present,
                "public_road": public_road,
                "time_of_day": time_of_day_map[time_of_day],
                "holiday": holiday,
                "school_season": school_season,
                "num_reported_accidents": num_reported_accidents
            }
        else:
            st.info("Veuillez remplir le formulaire et soumettre pour obtenir une prédiction.")
            return None




        