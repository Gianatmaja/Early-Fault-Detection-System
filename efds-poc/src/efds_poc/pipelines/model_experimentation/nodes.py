"""
This is a boilerplate pipeline 'model_experimentation'
generated using Kedro 0.18.14
"""

import numpy as np
import pandas as pd
import wandb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV, StratifiedKFold, ParameterGrid
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler


def split_data(df):

    # Get X and y
    y = df['class']
    X = df.drop(['class', 'timestamp'], axis = 1)

    # Train and test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

    # Scaling
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Tidy up
    X_train = pd.DataFrame(X_train, columns = ['P-PDG', 'P-TPT', 'T-TPT', 'P-MON-CKP', 'T-JUS-CKP'])
    X_test = pd.DataFrame(X_test, columns = ['P-PDG', 'P-TPT', 'T-TPT', 'P-MON-CKP', 'T-JUS-CKP'])

    X_train.reset_index(inplace = True)
    X_train.drop('index', axis = 1, inplace = True)

    X_test.reset_index(inplace = True)
    X_test.drop('index', axis = 1, inplace = True)

    X_train['class'] = y_train.values
    X_test['class'] = y_test.values

    return X_train, X_test


def train_rf_models(X_train, X_test):

    # Login to WANDB
    wandb.login()

    # Get X and y
    y_train = X_train['class']
    y_test = X_test['class']

    X_train.drop('class', axis = 1, inplace = True)
    X_test.drop('class', axis = 1, inplace = True)

    # Define hyperparameters
    grid_values = {'n_estimators': [200, 300, 400], 'max_depth': [2, 3, 4, 5]}

    # Define algorithm
    rf = RandomForestClassifier(max_features = int(X_train.shape[1]/3), random_state=1)

    # Perform stratified 5-fold cross-validation to get optimal hyperparameters
    cross_validation = StratifiedKFold(n_splits = 5)

    # Iterate through hyperparameter combinations
    for params in ParameterGrid(grid_values):
        # Create a new run for each combination
        with wandb.init(project="EFDS_POC", job_type = "hyperparameter_tuning_rf", config = params):
            wandb.run.config["model_name"] = "Random Forest"
            # Train a Random Forest model with the current hyperparameters
            #wandb.run.summary['Model'] = 'Random Forest'
            rf.set_params(**params)
            rf.fit(X_train, y_train)

            # Predict on the test set
            y_pred_rf = rf.predict(X_test)

            # Calculate and log metrics
            classification_rep = classification_report(y_test, y_pred_rf, output_dict = True)
            wandb.run.summary.update(params)
            wandb.run.summary.update(classification_rep)

    # Finish the WandB run
    wandb.finish()

    return None

def train_xgb_models(X_train, X_test):

    # Login to WANDB
    wandb.login()

    # Get X and y
    y_train = X_train['class']
    y_test = X_test['class']

    X_train.drop('class', axis = 1, inplace = True)
    X_test.drop('class', axis = 1, inplace = True)

    # Define hyperparameters
    grid_values = {'n_estimators': [100, 300, 500], 'max_depth': [3, 5, 7, 10]}

    # Define algorithm
    xgb = XGBClassifier(random_state = 1)

    # Perform stratified 5-fold cross-validation to get optimal hyperparameters
    cross_validation = StratifiedKFold(n_splits = 5)

    # Iterate through hyperparameter combinations
    for params in ParameterGrid(grid_values):
        # Create a new run for each combination
        with wandb.init(project="EFDS_POC", job_type = "hyperparameter_tuning_xgb", config = params):
            wandb.run.config["model_name"] = "XGBoost"
            # Train a Random Forest model with the current hyperparameters
            #wandb.run.summary['Model'] = 'Random Forest'
            xgb.set_params(**params)
            xgb.fit(X_train, y_train)

            # Predict on the test set
            y_pred_xgb = xgb.predict(X_test)

            # Calculate and log metrics
            classification_rep = classification_report(y_test, y_pred_xgb, output_dict = True)
            wandb.run.summary.update(params)
            wandb.run.summary.update(classification_rep)

    # Finish the WandB run
    wandb.finish()

    return None

