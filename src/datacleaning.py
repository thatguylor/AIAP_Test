import pandas as pd 
import numpy as np 
from logger import *

def DataCleaning(df,pathtosummary,pathtocsv): 
    df.drop_duplicates(subset ="ID", keep = 'first', inplace = True)

    df['Survive'] = df['Survive'].map({'Yes':'Yes', 'No':'No', '1':'Yes','0':'No'})

    df['Smoke'] = df['Smoke'].str.upper()  
    df.Smoke = df.Smoke.map({'YES':'Yes','NO':'No'})

    df = df[df.Age >0]  
    df = df[df.Age < 100]

    df['Ejection Fraction'] = df['Ejection Fraction'].map({'Low':'Low','Normal':'Normal','High':'High','L':'Low','N':'Normal'})

    df = df.fillna(method="ffill")

 ## Loggging summary to make sure ETL runs successfully 
    logging(df,pathtosummary)
 ## Write cleaned df to csv file 
    df.to_csv(pathtocsv)

    return df 