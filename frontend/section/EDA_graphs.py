import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os
import sys
from backend.data_loader import load_data
from backend.preprocessing import feature_engineering


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def app():
    train = load_data("train.csv")
    st.title("Analyse Exploratoire des Données (EDA)")
    st.write("""Explorez les données des accidents de la route à travers diverses visualisations
             """)
    st.subheader("Aperçu des données")
    st.dataframe(train)

    st.subheader("Aperçu des données apres traitement")
    train_processed = feature_engineering(train)
    st.dataframe(train_processed)
    