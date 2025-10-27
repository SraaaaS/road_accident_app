import pandas as pd
from loguru import logger
import os
from pathlib import Path
import streamlit as st

@st.cache_data
def load_data(file_name: str) -> pd.DataFrame:
    """
    Charge les données à partir d'un fichier CSV.

    Args:
        file_name (str): Le nom du fichier CSV à charger.

    Returns:
        pd.DataFrame: Les données chargées sous forme de DataFrame pandas.
    """
    logger.info(f"Chargement des données depuis le fichier: {file_name}")
    data_path = Path("data") / file_name
    if not data_path.exists():
        logger.error(f"Le fichier {file_name} n'existe pas dans le repertoire data")
        raise FileNotFoundError(f"Le fichier {file_name} n'existe pas.")
    data = pd. read_csv(data_path)
    logger.info(f"Données chargées avec succès. Dimensions des données: {data.shape}")
    return data