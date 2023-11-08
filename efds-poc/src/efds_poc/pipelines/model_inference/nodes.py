"""
This is a boilerplate pipeline 'model_inference'
generated using Kedro 0.18.14
"""

import numpy as np
import pandas as pd
import pickle

def predict_new_data(df, df_ref, model, scaler):
    # Define columns to preprocess
    to_drop = ['T-JUS-CKGL', 'QGL', 'P-JUS-CKGL']
    to_impute_med = ['T-TPT', 'P-MON-CKP']
    to_impute_mean = ['T-JUS-CKP']

    # Drop NA columns
    df.drop(to_drop, axis = 1, inplace = True)

    # Imputations
    for col in to_impute_med:
        med_imp = df_ref[col].median()
        df[col] = df[col].fillna(med_imp)

    for col in to_impute_mean:
        mean_imp = df_ref[col].mean()
        df[col] = df[col].fillna(mean_imp)

    # Tidy up df
    df.dropna(inplace = True)
    df.reset_index(inplace = True)
    df.drop('index', axis = 1, inplace = True)

    y = df['class']
    X_vals = df.drop(['timestamp', 'class'], axis = 1)

    # Scale data
    X_vals = scaler.transform(X_vals)
    X_vals = pd.DataFrame(X_vals, columns = ['P-PDG', 'P-TPT', 'T-TPT', 'P-MON-CKP', 'T-JUS-CKP'])

    # Predictions
    y_preds = model.predict(X_vals)

    df['predicted'] = y_preds

    return df