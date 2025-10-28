import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os
import sys
from backend.data_loader import load_data
from backend.preprocessing import feature_engineering
from loguru import logger


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))




def app():
    train = load_data("train.csv")
    train_processed = feature_engineering(train)

    st.markdown("<p style='color:#307D7E; font-size:34px; font-weight:bold'>Analyse Exploratoire des Données (EDA)", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px'>Explorez les données des accidents de la route à travers diverses visualisations.", unsafe_allow_html=True)
    
    colonnes_numeriques = ["curvature", "accident_risk", "curvature_speed_interaction", "accidents_per_lane", 
                           "curvature_per_lane", "speed_per_lane"]
    
    colonnes_cat = ["road_type", "num_lanes", "speed_limit", "lighting", "weather", "road_signs_present", 
                    "public_road", "time_of_day", "holiday", "school_season", "num_reported_accidents"]
    
    tab_des_deux = pd.concat( [train[["curvature", "accident_risk"]], train_processed[["curvature_speed_interaction", 
                                "accidents_per_lane", "curvature_per_lane", "speed_per_lane"]] ], axis=1) 


    #Affichage du tableau de données initial
    st.markdown("<p style='color:#307D7E; font-size:20px; font-weight:bold'>Données brutes", unsafe_allow_html=True)
    st.dataframe(train)

    #Affichage du tableau des données processed
    
    st.markdown("<p style='color:#307D7E; font-size:20px; font-weight:bold'>Données après traitement", unsafe_allow_html=True)
    st.dataframe(train_processed)

    st.divider()
    #Affichage des colonnes numériques
    st.markdown("<p style='color:#307D7E; font-size:20px; font-weight:bold'>Noms des colonnes numériques :", unsafe_allow_html=True)
    st.markdown(", ".join(f"`{col}`" for col in colonnes_numeriques))

    st.divider()
    #Affichage des colonnes catégorielles
    st.markdown("<p style='color:#307D7E; font-size:20px; font-weight:bold'>Noms des colonnes catégorielles :", unsafe_allow_html=True)
    st.markdown(", ".join(f"`{col}`" for col in colonnes_cat))

    st.divider()
    #Visualisation des variables
    st.markdown("<p style='color:#307D7E; font-size:20px; font-weight:bold'>Visualisation des variables", unsafe_allow_html=True)
    choice_type = st.radio("Choisissez le type de variables à afficher :", ["Numériques", "Catégorielles"])

    if choice_type == "Numériques":
        variable = st.selectbox("Choisissez une variable numérique :", colonnes_numeriques)
        fig, ax = plt.subplots(figsize=(4, 3))
        sns.histplot(tab_des_deux, x=variable, bins=50, color="#B65FCF", ax=ax)
        ax.set_title(f"Distribution de la variable '{variable}'", fontsize=11, color="#4B0082")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    elif choice_type == "Catégorielles":
        variable = st.selectbox("Choisissez une variable catégorielle :", colonnes_cat)
        color = sns.color_palette("BuPu")
        fig, ax = plt.subplots(figsize=(4, 3))
        if train[variable].nunique() <= 6:
            ax.pie(train[variable].value_counts(), labels=train[variable].unique(), colors=color, autopct='%1.1f%%')
        else:
            sns.countplot(data=train, x=variable, palette="YlGnBu", ax=ax)
            ax.tick_params(axis='x', rotation=30)
        ax.set_title(f"Répartition de '{variable}'", fontsize=9, color="#4B0082")
        st.pyplot(fig)
        plt.close(fig)

    st.divider()
    #Correlation heatmap
    st.markdown("<p style='color:#307D7E; font-size:20px; font-weight:bold'>Corrélation des variables numériques avec le risque d'accident", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(6, 5))  
    sns.heatmap(train_processed.corr()[["accident_risk"]].sort_values(by="accident_risk", ascending=False), 
                annot=True, center=0, cmap="YlGnBu", ax=ax)
    ax.set_title("Matrice de corrélation - Heatmap", fontsize=11, color="#4B0082")
    st.pyplot(fig)