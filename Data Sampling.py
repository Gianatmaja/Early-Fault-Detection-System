#!/usr/bin/env python
# coding: utf-8

# # Data Samping
# 
# This notebook goes through the sampling process for the complete 3W dataset. The objective is to obtain a compiled dataset consisting of the various faults in oil wells, while still keeping the overall size of the dataset at an acceptable level.
# 
# For more information on the dataset, visit the 3W Dataset GitHub Repository (https://github.com/ricardovvargas/3w_dataset/).

# Import required libraries
import os
import pandas as pd

# Parent folders containing subfolders
parent_folders = ['data/data01', 'data/data02', 'data/data03', 'data/data04']

# Initialize an empty list to store the dataframes
dfs = []

# Change as required
n_samples = 5

# Go through each parent folder
for parent_folder in parent_folders:
    # Iterate through subfolders in the parent folder
    for subfolder in os.listdir(parent_folder):
        subfolder_path = os.path.join(parent_folder, subfolder)

        if os.path.isdir(subfolder_path):
            # Initialize dataframes list for each subfolder
            subfolder_dfs = []

            # Loop through each CSV file in the subfolder
            for filename in os.listdir(subfolder_path):
                if filename.endswith('.csv'):
                    file_path = os.path.join(subfolder_path, filename)
                    # Read the CSV file into a DataFrame
                    df = pd.read_csv(file_path)

                    # Filter rows where 'target' is 0 and 10X, and sample n_samples rows for each
                    try:
                        df_target_0 = df[df['class'] == 0].sample(n = n_samples, random_state = 1)
                        df_target_1 = df[df['class'] > 100].sample(n = n_samples, random_state = 1)

                        # Check if there are enough rows for both target values
                        if len(df_target_0) == n_samples and len(df_target_1) == n_samples:
                            # Concatenate the filtered and sampled DataFrames
                            final_df = pd.concat([df_target_0, df_target_1])

                            # Append the final DataFrame to the subfolder_dfs list
                            subfolder_dfs.append(final_df)
                    except:
                        pass

            # Concatenate all the DataFrames from different files into a single DataFrame for the subfolder
            if subfolder_dfs:
                subfolder_result = pd.concat(subfolder_dfs)
                # Append the subfolder result to the main list of DataFrames
                dfs.append(subfolder_result)

# Concatenate all the DataFrames from different subfolders into a single DataFrame
final_result = pd.concat(dfs)

# Tidy up df
df_final = final_result.sort_values(by = ['timestamp', 'class']).reset_index().drop('index', axis = 1)

# Counts of each class
df_final['class'].value_counts()

df_final['class'].replace({101:1, 102:2, 105:3, 106:4, 107:5, 108:6}, inplace=True)
df_final['class'] = df_final['class'].astype('int')

df_final.to_csv('3W_Sampled.csv', index = False)
