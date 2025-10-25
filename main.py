import streamlit as st
import joblib
from loguru import logger

from backend.EDA import eda
from backend.data_loader import load_data
from backend.preprocessing import feature_engineering
from backend.models import train_and_select_models, save_best_model, predict

train = load_data("train.csv")
test = load_data("test.csv")

logger.info("EDA des données d'entraînement en cours...")
eda(train)
logger.info("EDA des données d'entraînement terminée.")

logger.info("Prétraitement des données d'entraînement en cours...")
train_processed = feature_engineering(train)
logger.info("Prétraitement des données d'entraînement terminé.")

logger.info("Entraînement et sélection du meilleur modèle en cours...")
best_model, best_model_name = train_and_select_models(train_processed)
logger.info("Entraînement et sélection du meilleur modèle terminés.")

logger.info("Sauvegarde du meilleur modèle en cours...")
save_best_model(best_model, best_model_name)
logger.info("Sauvegarde du meilleur modèle terminée.")

logger.info("Prétraitement des données de test en cours...")
test_processed = feature_engineering(test)
logger.info("Prétraitement des données de test terminé.")

logger.info("Prédictions sur les données de test en cours...")
predictions = predict(best_model, test_processed)
logger.info("Prédictions sur les données de test terminées.")




#logger.info("Démarrage de l'application Streamlit")




