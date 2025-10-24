import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from loguru import logger


def eda(df):

    #Observations initiales des données
    logger.info(f"Dimensions initiales des données: {df.shape}", )

    logger.info("Indices des colonnes et leurs noms:\n")
    dic = {}
    for i, k in enumerate(list(df.columns)):
        dic[i]=k
        logger.info(f"{i} : {k}")

    logger.info(f"Les colonnes et leurs types : \n\n{df.dtypes}")

    logger.info(f"Nombre de valeurs manquantes par colonne: \n\n{df.isna().sum()}")
    
    logger.info("Analyse exploratoire des données en cours...")

#Colonnes numériques
    logger.info("Traitement des colonnes numériques:\n")
    colonnes_numeriques = df.select_dtypes(["number"]).columns.to_list()
    logger.info("Les  colonnes numeriques : \n")
    for k in colonnes_numeriques:
        logger.info(f"- {k}")

    liste_indice_col_num = []
    for ele in colonnes_numeriques:
        for cle, val in dic.items():
            if ele==val:
                liste_indice_col_num.append(cle)
    logger.info(f"Les indices de colonnes numériques : {liste_indice_col_num}") 

    #a verifier
    logger.info("Visualisation de la distribution des colonnes de variables numériques:\n")
    # colonnes_numeriques = df[[k for k in list(colonnes_numeriques)]] 

    # plt.figure(figsize=(15,10))
    # for i, col in enumerate(list(colonnes_numeriques.columns),1):
    #     plt.subplot(2,3,i)
    #     sns.histplot(colonnes_numeriques[col], bins=30, color="purple")
    #     plt.title(f"Distribution de {col}")
    # plt.tight_layout()
    # plt.show()
    
    num_features =  df.select_dtypes(["float64"]).columns.tolist()

    #Histogramme
    plt.figure(figsize=(10,5))
    for i, col in enumerate(num_features,1):
        plt.subplot(1,2,i)
        sns.histplot(df, x=col, bins=50, color="#B65FCF")
        plt.title(f"Distribution de la variable '{col}'")
    plt.tight_layout()
    logger.info("Visualisation de la distribution des colonnes de variables numériques:\n")
    plt.show()

    #Relations entre les variables numériques (pairplot)
    plt.figure()
    sns.pairplot(df[num_features].sample(500), diag_kind = "kde")
    plt.suptitle("Relations entre les variables numeriques", y=1.02)
    plt.show()

#Colonnes des variables discrètes
    logger.info("Traitement des colonnes discrètes:\n")
    discrete_features = ['num_lanes', 'speed_limit', 'num_reported_accidents']

    #Histogramme
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(discrete_features, 1):
        plt.subplot(1, 3, i)
        sns.countplot(data=df, x=col, palette="BuPu")
        plt.title(f"Répartition de {col}")
    plt.tight_layout()
    logger.info("Visualisation de la distribution des colonnes de variables discretes -Histogramme\n")
    plt.show()
    #Pie Chart
    color = sns.color_palette("PuOr")
    plt.figure(figsize=(15,10))
    for i, col in enumerate(discrete_features, 1):
        plt.subplot(2,2,i)
        plt.pie(x=list(df[col].value_counts()), colors=color,labels=df[col].unique(),autopct='%1.1f%%')
        plt.title(f"Repartition de la variable {col}")
    logger.info("Visualisation de la distribution des colonnes de variables discretes - Pie Chart\n")
    plt.show()

    #Matrice de correlation (Heatmap)
    logger.info("Matrice de correlation des variables numeriques:\n")
    plt.figure()
    sns.heatmap(data= df[colonnes_numeriques].corr(), annot=True, cmap="YlGnBu" )
    plt.suptitle("Heatmap")
    logger.info("Visualisation de la distribution des correlations entre toutes les variables numeriques - Heatmap\n")
    plt.show()

#Colonnes des variables catégorielles (booléennes et textuelles)
    colonnes_bool = df.select_dtypes(["bool"]).columns.to_list()
    logger.info(f"Les  colonnes de booléens : \n")
    for k in colonnes_bool:
        logger.info(f"- {k}")

    liste_indice_col_bool = []
    for ele in colonnes_bool:
        for cle, val in dic.items():
            if ele==val:
                liste_indice_col_bool.append(cle)
    logger.info(f"Les indices de colonnes de booleens : {liste_indice_col_bool}")

    #Pie Chart
    color = sns.color_palette("crest")
    plt.figure(figsize=(15,10))
    for i, col in enumerate(colonnes_bool, 1):
        plt.subplot(2,2,i)
        plt.pie(x=list(df[col].value_counts()), colors=color,labels=[True, False],autopct='%1.1f%%')
        plt.title(f"Repartition de la variable '{col}'")
    logger.info("Visualisation de la distribution des colonnes de variables booleennes - Pie Chart\n")
    plt.show()


    colonnes_categorielles = df.select_dtypes(["object"]).columns.to_list()
    logger.info("Les  colonnes catégorielles : \n")
    for k in colonnes_categorielles:
        logger.info(f"- {k}")

    liste_indice_col_cat = []
    for ele in colonnes_categorielles:
        for cle, val in dic.items():
            if ele==val:
                liste_indice_col_cat.append(cle)
    logger.info(f"Les indices de colonnes booleens : {liste_indice_col_cat}")

    logger.info("Valeurs uniques composant chaque colonne categorielles : \n")
    for cat in colonnes_categorielles :
        logger.info(f" - {cat} : {df[cat].unique()}")

    #Pie Chart
    plt.figure(figsize=(15,10))
    color = sns.color_palette("BuPu")
    for i, col in enumerate(colonnes_categorielles, 1):
        plt.subplot(2,2,i)
        label=df[col].unique()
        plt.pie(x=df[col].value_counts(), labels=label, colors=color, autopct='%1.1f%%')
        plt.title(f"Répartion de la variable {col}")
    plt.show()
    logger.info("Visualisation de la distribution des colonnes de variables categorielles - Pie Chart\n")
    logger.info("Analyse exploratoire des données terminée.")




    



