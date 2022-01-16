#!/usr/bin/env python
import os
import pandas as pd
import time
from datacleaning import * 
from databaseconnect import *
from logger import * 
from gradientboosting import *
from logisticregression import * 
from randomforest import * 

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '..', 'data', 'survive.db')
datasummary = os.path.join(dirname, '..', 'data', 'Dataset_Summary.txt')
cleandatasummary = os.path.join(dirname, '..', 'data', 'Cleaned_Dataset_Summary.txt')
cleaneddata = os.path.join(dirname, '..', 'data', 'Cleaned_Data.csv')

#Execute Extract part of ETL 
print("="*20)
print("Begin Connection to Database and Extraction of Data")
print("="*20)
time.sleep(10)
df = pd.read_sql_query("SELECT * from survive", ConnectToDB(filename))
time.sleep(10)
#Execute Logging Once dataframe is loaded
print("="*20)
logging(df,datasummary)
print("="*20)
time.sleep(10)
#Execute Transform part of ETL and Logging is executed
print("="*20)
print("Now Commencing Cleaning of dataset")
print("="*20)
time.sleep(10)
print("="*20)
df = DataCleaning(df,cleandatasummary,cleaneddata)
print("="*20)
time.sleep(10)
#Execute Loading and Transforming of data pipeline to encoded variables 
flag = False
while flag is False:
    print("For Machine Learning Model Selection, choose 0 for Logistic Regression, 1 for Random Forest and 2 for Gradient Boosting, Press q to quit")
    choice = input("Enter your choice of Machine Learning Algorithm:")
    if choice == '0':
        logisticRegression(df)
    elif choice == '1':
        randomForest(df)
    elif choice == '2':
        gradientBoost(df)
    elif choice == 'q':
        flag = True
    else: print("Your choice is not valid, please select again")
