import sqlite3
import pandas as pd 
import numpy as np 

def ConnectToDB(pathtodb):
    try:
        sqliteConnection = sqlite3.connect(pathtodb)
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    return sqliteConnection



def DataCleaning(df,pathtosummary): 
    df = df.drop_duplicates(subset ="ID", keep = 'first', inplace = True)

    df.Survive = df.Survive.map({'Yes':1, 'No':0, '1':1,'0':0})

    df.Gender = df.Gender.map({'Male':1,'Female':0})

    df['Smoke'] = df['Smoke'].str.upper()  
    df.Smoke = df.Smoke.map({'YES':1,'NO':0})

    df = df[df.Age >0]  
    df = df[df.Age < 100]

    df['Ejection Fraction'] = df['Ejection Fraction'].map({'Low':'Low','Normal':'Normal','High':'High','L':'Low','N':'Normal'})

    df = df.fillna(method="ffill")

 ## Loggging summary to make sure ETL runs successfully 
    file = open(pathtosummary,"r+")
    file.truncate(0)
    file.close()

    for column in df:
        file = open(pathtosummary,"a")
        file.write(str(df[column].value_counts()))
        file.write('\n')
        file.write('='*20)
        file.write('\n')
        file.close()


