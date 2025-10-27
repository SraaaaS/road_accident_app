import joblib 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from loguru import logger
from pathlib import Path
import os

def train_and_select_models(df):

    X_train = df.drop(columns=["accident_risk"])
    y_train = df["accident_risk"]

    X, X_valid, y, y_valid = train_test_split(
        X_train, y_train, test_size=0.2, random_state=42
    )


    models = {
    "RandomForest": RandomForestRegressor(),
    "CatBoost": CatBoostRegressor(verbose=0),
    "XGBRegressor": XGBRegressor(),
    "LGBMRegressor": LGBMRegressor(),
    "LinearRegression": LinearRegression(),
    "GradientBoosting": GradientBoostingRegressor()
    }


    best_rmse = float("inf")
    best_model = None

    for nom, modele in models.items():
        modele.fit(X, y)
        preds = modele.predict(X_valid)
        rmse = np.sqrt(mean_squared_error(y_valid, preds))
        logger.info(f"RMSE pour le modele {nom} : {rmse:.5f}")

        if rmse < best_rmse:
            best_rmse = rmse
            best_model = modele
            nom_du_modele = nom

    logger.info(f"Le meilleur modele est {nom_du_modele} avec un RMSE de {best_rmse:.5f}")  
    return best_model, nom_du_modele


def save_best_model(model, model_name):
    model_dir = Path("models") 
    model_dir.mkdir(exist_ok=True)
    model_path =model_dir / f"{model_name}.pkl"
    joblib.dump(model, model_path)
    logger.info(f"Modèle sauvegardé sous {model_path}")


def predict(model, data):
    predictions = model.predict(data)
    return predictions
