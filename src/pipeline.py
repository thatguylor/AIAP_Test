#!/usr/bin/env python

import os,sys
import pandas as pd
import numpy as np 
from sklearn.compose import make_column_selector as selector
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from datacleaning import * 
from databaseconnect import *
from logger import * 

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '..', 'data', 'survive.db')
datasummary = os.path.join(dirname, '..', 'data', 'Dataset_Summary.txt')
cleandatasummary = os.path.join(dirname, '..', 'data', 'Cleaned_Dataset_Summary.txt')
cleaneddata = os.path.join(dirname, '..', 'data', 'Cleaned_Data.csv')

#Execute Extract part of ETL 
df = pd.read_sql_query("SELECT * from survive", ConnectToDB(filename))
#Execute Logging Once dataframe is loaded 
logging(df,datasummary)
#Execute Transform part of ETL and Logging is executed
print("Now Commencing Cleaning of dataset")
df = DataCleaning(df,cleandatasummary,cleaneddata)
#Execute Loading and Transforming of data pipeline to encoded variables 
print("Now Commencing Pipeline Transformation")

target_name = "Survive"
target = df[target_name]
dataset = df.drop(columns=[target_name,"ID"])

numerical_columns_selector = selector(dtype_exclude=object)
categorical_columns_selector = selector(dtype_include=object)

numerical_columns = numerical_columns_selector(dataset)
categorical_columns = categorical_columns_selector(dataset)

categorical_preprocessor = OneHotEncoder(handle_unknown="ignore")
numerical_preprocessor = StandardScaler()

preprocessor = ColumnTransformer([
    ('one-hot-encoder', categorical_preprocessor, categorical_columns),
    ('standard_scaler', numerical_preprocessor, numerical_columns)])

model = make_pipeline(preprocessor, LogisticRegression(max_iter=500))

data_train, data_test, target_train, target_test = train_test_split(
    dataset, target, random_state=42)

_= model.fit(data_train, target_train)

print(model.predict(data_test)[:5])
print(target_test[:5])
print(model.score(data_test, target_test))