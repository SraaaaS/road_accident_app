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
    st.title("Analyse Exploratoire des Données (EDA)")
    st.write("""Explorez les données des accidents de la route à travers diverses visualisations
             """)

    #Affichage du tableau de données initial
    st.subheader("Aperçu des données")
    st.dataframe(train)

    #Affichage du tableau des données processed
    st.subheader("Aperçu des données apres traitement")
    train_processed = feature_engineering(train)
    st.dataframe(train_processed)

    #Affichage de la repartition des variables numeriques
    colonnes_numeriques = train_processed.select_dtypes(["number"]).columns
    st.subheader("Les colonnes numeriques du tableau de données utilisé pour la prévision")
    logger.info(f"Les  colonnes numeriques : \n")
    for k in colonnes_numeriques:
        logger.info(f"- {k}")

    #Histogramme des variables numeriques
    num_features = train_processed.select_dtypes(["float64"]).columns
    st.subheader("Histogramme des variables numeriques")
    plt.figure(figsize=(10,5))
    for i, col in enumerate(num_features,1):
        plt.subplot(1,2,i)
        sns.histplot(train_processed, x=col, bins=50, color="#B65FCF")
        plt.title(f"Distribution de la variable '{col}'")
    plt.tight_layout()
    st.pyplot()

    #Affichage de la repartition des variables categorielles
    colonnes_cat = train.select_dtypes(["bool","int64"]).columns
    st.subheader("Les colonnes categorielles du tableau de données utilisé pour la prévision")
    logger.info(f"Les  colonnes categorielles : \n")
    for k in colonnes_cat:
        logger.info(f"- {k}")
    
    logger.info("Valeurs uniques composant chaque colonne categorielles : \n")
    st.subheader("Les valeurs uniques composant chaque colonne categorielle")
    for cat in colonnes_cat :
        logger.info(f" - {cat} : {train[cat].unique()}")
    
    discrete_features = ['num_lanes', 'speed_limit', 'num_reported_accidents']

    #Repartition en barplot d'une selection de variables categorielles qui s'y pretent
    
    st.subheader("Répartition des variables catégorielles")
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(discrete_features, 1):
        plt.subplot(1, 3, i)
        sns.countplot(data=train, x=col, palette="BuPu")
        plt.title(f"Répartition de {col}")
    plt.tight_layout()
    st.pyplot()

    #Repartition du reste des colonnes categorielles en pie chart
    plt.figure(figsize=(15,10))
    color = sns.color_palette("BuPu")
    colonnes = ["road_type", "lighting", "weather", "time_of_day"]
    for i, col in enumerate(colonnes, 1):
        plt.subplot(2,2,i)
        label=train[col].unique()
        plt.pie(x=train[col].value_counts(), labels=label, colors=color, autopct='%1.1f%%')
        plt.title(f"Répartion de la variable {col}")
    st.pyplot()

    #Repartition des colonnes de booleens
    color = sns.color_palette("crest")
    plt.figure(figsize=(15,10))
    booleens = ["road_signs_present", "public_road", "holiday", "school_season"]
    for i, col in enumerate(booleens, 1):
        plt.subplot(2,2,i)
        plt.pie(x=list(train[col].value_counts()), colors=color,labels=[True, False],autopct='%1.1f%%')
        plt.title(f"Repartition de la variable '{col}'")
    st.pyplot()
    
        
    
        
        
