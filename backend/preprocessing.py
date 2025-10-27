import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from loguru import logger
import streamlit as st

@st.cache_data
def feature_engineering(data):

    data_encoded = data.copy()

    # Binning des variables continues
    logger.info("Binning des variables continues 'curvature' et 'speed_limit'")
    #3 categories de courbure: faible (entre 0 et 0.33), moyenne (entre 0.33 et 0.66) et forte (entre 0.66 et 1).
    data_encoded["curvature"] = pd.cut(
        data["curvature"],
        bins=3,
        labels=["faible", "moyenne", "forte"]
    )

    #2 categories de limite de vitesse: faible (<=50) et élevée (>50).
    data_encoded["speed_limit"] = pd.cut(
        data["speed_limit"],
        bins=2,
        labels=["faible", "elevee"]
    )

    col_categorielle = ['road_type', 'lighting', 'weather', 'time_of_day', 'curvature', 'speed_limit']
    
    # One-Hot Encoding des variables catégorielles
    logger.info("Application du One-Hot Encoding sur les variables catégorielles")
    encoder = OneHotEncoder(sparse_output=False)
    encoded = encoder.fit(data_encoded[col_categorielle])
    encoded = encoder.transform(data_encoded[col_categorielle])
    data_final = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(col_categorielle))
    data_final = pd.concat([data.drop(columns=col_categorielle).reset_index(drop=True), 
                            data_final.reset_index(drop=True)], axis=1)
    logger.info("Fin du One-Hot Encoding sur les variables catégorielles")

    # Conversion des colonnes booléennes en entiers (0 et 1)
    logger.info("Conversion des colonnes booléennes en entiers (0 et 1)")
    colonnes_bool = ['road_signs_present', 'public_road', 'holiday', 'school_season']
    data_final[colonnes_bool] = data_final[colonnes_bool].astype('int')
    logger.info("Fin de la conversion des colonnes booléennes en entiers (0 et 1)")

    # Création de nouvelles features
    logger.info("Création de nouvelles features")
    data_final["curvature_speed_interaction"] = data["curvature"] * data["speed_limit"]
    data_final["accidents_per_lane"] = data["num_reported_accidents"] / (data["num_lanes"] + 1e-3)
    data_final["curvature_per_lane"] = data["curvature"] / (data["num_lanes"] + 1e-3)
    data_final["speed_per_lane"] = data["speed_limit"] / (data["num_lanes"] + 1e-3)
    logger.info("Fin de la création de nouvelles features")

    return data_final
