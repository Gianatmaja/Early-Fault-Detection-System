"""
This is a boilerplate pipeline 'model_saving'
generated using Kedro 0.18.14
"""

import numpy as np
import pandas as pd
import wandb
import pickle
import os

from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from explainerdashboard import ClassifierExplainer, ExplainerDashboard

def save_scaler(df):

    # Get X and y
    y = df['class']
    X = df.drop(['class', 'timestamp'], axis = 1)

    # Train and test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

    # Scaling
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)

    return scaler


def save_model(df):

    api = wandb.Api()

    # Best acc model details
    best_acc_path = '<Replace with path to best performing model - can be found in wandb dashboard>'
    run = api.run(best_acc_path)
    config = run.config

    print(config)

    # Get X and y
    y = df['class']
    X = df.drop('class', axis = 1)

    # Train best model with full training data
    if config['model_name'] == 'Random Forest':
        best = RandomForestClassifier(max_depth = config['max_depth'], n_estimators = config['n_estimators'], random_state = 1)
        best.fit(X, y)
    else:
        best = XGBClassifier(max_depth = config['max_depth'], n_estimators = config['n_estimators'], random_state = 1)
        best.fit(X, y)

    return best


def explain_model(model, df):

    # Get X and y
    y = df['class']
    X = df.drop('class', axis = 1)

    # Explain model and show explainer dashboard
    explainer = ClassifierExplainer(model, X, y)
    ExplainerDashboard(explainer).run()

    return None