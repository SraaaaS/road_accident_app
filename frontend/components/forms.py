import streamlit as st

def risk_form():
    with st.form(key='risk_form'):
        st.write("Veuillez entrer les paramètres pour prédire le risque d'accident :")

        st.subheader("Conditions routières:")

        road_type = st.selectbox("Type de route", 
                                ["Autoroute", "Route de Ville", "Route de campagne"])
        lightining = st.selectbox("Conditions d'éclairage",
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
        num_reported_accidents = st.selectbox("Nombre d'accidents signalés dans la zone", 0, 4, 1)

                                         
        submitted = st.form_submit_button(label='Prédire le risque d\'accident')
        if submitted==True:
            st.success("Données entrées avec succès! Préparation de la prédiction...")
            return {
                "Type de route": road_type,
                "Conditions d'éclairage": lightining,
                "Conditions météorologiques": weather,
                "Moment de la journée": time_of_day,
                "Courbure de la route": curvature,
                "Nombre de voies": num_lanes,
                "Limite de vitesse": speed_limit,
                "Présence de panneaux de signalisation": road_sign_present,
                "Route publique": public_road,
                "Jour férié": holiday,
                "Saison scolaire": school_season,
                "Nombre d'accidents signalés dans la zone": num_reported_accidents
            }
        else:
            st.info("Veuillez remplir le formulaire et soumettre pour obtenir une prédiction.")
            return None




        