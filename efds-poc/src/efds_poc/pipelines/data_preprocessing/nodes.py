"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.14
"""

import numpy as np
import pandas as pd
import dtale
from datetime import datetime


def auto_eda(df):

    # Current date
    current_time = datetime.now()

    # Convert to a string
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Print notice to user
    print(current_time_str, '\033[91mIMPORTANT\033[0m    - Press Ctrl + C to exit the Auto-EDA process.')

    # Auto-EDA process
    d = dtale.show(df, subprocess=False)

    return None


def preproc_data(df):

    # Define columns to preprocess
    to_drop = ['T-JUS-CKGL', 'QGL', 'P-JUS-CKGL']
    to_impute_med = ['T-TPT', 'P-MON-CKP']
    to_impute_mean = ['T-JUS-CKP']

    # Drop NA columns
    df.drop(to_drop, axis = 1, inplace = True)

    # Imputations
    for col in to_impute_med:
        df[col] = df[col].fillna(df[col].median())

    for col in to_impute_mean:
        df[col] = df[col].fillna(df[col].mean())

    # Tidy up df
    df.dropna(inplace = True)
    df.reset_index(inplace = True)
    df.drop('index', axis = 1, inplace = True)

    return df


