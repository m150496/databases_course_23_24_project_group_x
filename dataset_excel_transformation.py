# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:07:39 2023

@author: Milan Cukovic
"""

import numpy as np
import pandas as pd

df = pd.read_csv('RAW_interactions.csv')
df_transformed_RAW_interactions = df.drop('date', axis=1)
df_transformed_RAW_interactions = df_transformed_RAW_interactions.drop('review', axis=1)
df_transformed_RAW_interactions.to_csv('RAW_interactions_processed.csv')

df = pd.read_csv('RAW_recipes.csv')
df_transformed_RAW_recipes = df.drop(columns = ['contributor_id', 'submitted', 'steps'], axis=1)
df_transformed_RAW_recipes['nutrition'] = df_transformed_RAW_recipes['nutrition'].apply(lambda x: x[1:-1].split(',')) #https://stackoverflow.com/questions/45758646/pandas-convert-string-into-list-of-strings
df_transformed_RAW_recipes['nutrition'] = df_transformed_RAW_recipes['nutrition'].apply(lambda listx: [float(value) for value in listx]) #https://iq.opengenus.org/python-lambda-for-loop/ 
df_transformed_RAW_recipes[['calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']] = pd.DataFrame(df_transformed_RAW_recipes['nutrition'].tolist())
df_transformed_RAW_recipes = df_transformed_RAW_recipes.drop(columns = ['nutrition'], axis=1)
df_transformed_RAW_recipes.to_csv('RAW_recipes_processed.csv')
