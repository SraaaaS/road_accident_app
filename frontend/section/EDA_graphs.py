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
    st.markdown("<p style='font-size:20px'>Explorez les données des accidents de la route à travers diverses visualisations", unsafe_allow_html=True)
    
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


    # elif choice_type == "Catégorielles":
    #     variable = st.selectbox("Choisissez une variable catégorielle :", colonnes_cat)
    #     color = sns.color_palette("BuPu")
    #     label = train[variable].unique()
    #     if train[variable].nunique() <= 6 :
    #         train[variable].value_counts().plot.pie(
    #             autopct='%1.1f%%', colors=color, ax=ax, ylabel=''
    #         )
    #     else:
    #         fig, ax = plt.subplots(figsize=(4, 3))
    #         sns.countplot(data=train, x=variable, palette="BuPu", ax=ax)
    #         plt.xticks(rotation=30)
    #     ax.set_title(f"Répartition de '{variable}'", fontsize=6, color="#4B0082")
    #     plt.tight_layout()
    #     st.pyplot(fig)
    #     plt.close(fig)


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


#------------------------------------------------------------------------------------------------
    # #Affichage de la repartition des variables numeriques
    # st.subheader("Les variables numeriques")
    # st.write("\n Les colonnes numeriques du tableau de données utilisé pour la prévision :")
    # logger.info(f"Les  colonnes numeriques : \n")
    # st.markdown(", ".join(f"`{col}`" for col in colonnes_numeriques))

    # #Histogramme des variables numeriques
    # st.markdown("### Histogramme des variables numeriques")
    # cols = st.columns(3)
    # plt.figure(figsize=(15,10))

    # for i, col in enumerate(colonnes_numeriques,1):
    #     with cols[i%3]:
    #         fig, ax = plt.subplots(figsize=(4, 3))
    #         sns.histplot(tab_des_deux, x=col, bins=50, color="#B65FCF", ax=ax)
    #         ax.set_title(f"Distribution de la variable '{col}'", fontsize=11, color="#4B0082")
    #         st.pyplot(fig)

    # #Affichage de la repartition des variables categorielles
    # st.write("\n Les colonnes categorielles du tableau de données utilisé pour la prévision")
    # logger.info(f"Les  colonnes categorielles : \n")
    # st.markdown(",".join(f"'{col}'" for col in colonnes_cat))
    
    # logger.info("Valeurs uniques composant chaque colonne categorielles : \n")
    # st.write("\n Les valeurs uniques composant chaque colonne categorielle")
    # for cat in colonnes_cat :
    #     st.write(f" - {cat} : {train[cat].unique()}")
    
    # discrete_features = ['num_lanes', 'speed_limit', 'num_reported_accidents']

    # #Repartition en barplot d'une selection de variables categorielles qui s'y pretent
    
    # st.markdown("### Barplot des variables catégorielles")
    # cols = st.columns(3)
    # for i, col in enumerate(discrete_features, 1):
    #     with cols[i%3]:
    #         fig, ax = plt.subplots(figsize=(4, 3))
    #         sns.countplot(data=train, x=col, palette="BuPu", ax=ax)
    #         ax.set_title(f"Répartition de '{col}'", fontsize=11, color="#4B0082")
    #         plt.xticks(rotation=30)
    #         st.pyplot(fig)

    # #Repartition du reste des colonnes categorielles en pie chart
    # st.markdown("### Pie Chart des autres variables catégorielles")
    # color = sns.color_palette("BuPu")
    # colonnes = ["road_type", "lighting", "weather", "time_of_day"]
    # cols = st.columns(2)
    # for i, col in enumerate(colonnes, 1):
    #     with cols[i%2]:
    #         fig, ax = plt.subplots(figsize=(4, 3))
    #         label=train[col].unique()
    #         plt.pie(x=train[col].value_counts(), labels=label, colors=color, autopct='%1.1f%%')
    #         ax.set_title(f"Répartion de la variable  '{col}'", fontsize=11, color="#4B0082")
    #         st.pyplot(fig)

    # #Repartition des colonnes de booleens
    # st.columns(2)
    # st.markdown("### Pie Chart des variables booléennes")
    # color = sns.color_palette("crest")

    # booleens = ["road_signs_present", "public_road", "holiday", "school_season"]
    # for i, col in enumerate(booleens, 1):
    #     with cols[i % 2]:
    #         fig, ax = plt.subplots(figsize=(4, 3))
    #         train[col].value_counts().plot.pie(
    #             autopct="%1.1f%%", colors=color, labels=[True, False], ax=ax,
    #             textprops={"fontsize": 9}
    #         )
    #         ax.set_ylabel("")
    #         ax.set_title(f"Répartition de '{col}'", fontsize=11, color="#4B0082")
    #         st.pyplot(fig)
        
    
       
