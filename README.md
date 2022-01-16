# AIAP Assessment - Batch 10
## Section A - Particulars
Chan Yao Kuan
chanyaokuan@gmail.com
github: https://github.com/thatguylor 

## Section B - Overview of Folder Structure - You may ignore the .git and .vscode settings, only the src and data folders are impt
📦AIAP_Test
 ┣ 📂data
 ┃ ┣ 📜Cleaned_Data.csv
 ┃ ┣ 📜Cleaned_Dataset_Summary.txt
 ┃ ┣ 📜Dataset_Summary.txt
 ┃ ┗ 📜survive.db
 ┣ 📂src
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜commonfunctions.cpython-39.pyc
 ┃ ┃ ┣ 📜databaseconnect.cpython-38.pyc
 ┃ ┃ ┣ 📜databaseconnect.cpython-39.pyc
 ┃ ┃ ┣ 📜datacleaning.cpython-38.pyc
 ┃ ┃ ┣ 📜datacleaning.cpython-39.pyc
 ┃ ┃ ┣ 📜evaluation.cpython-38.pyc
 ┃ ┃ ┣ 📜gradientboosting.cpython-38.pyc
 ┃ ┃ ┣ 📜logger.cpython-38.pyc
 ┃ ┃ ┣ 📜logger.cpython-39.pyc
 ┃ ┃ ┣ 📜logisticregression.cpython-38.pyc
 ┃ ┃ ┗ 📜randomforest.cpython-38.pyc
 ┃ ┣ 📜databaseconnect.py
 ┃ ┣ 📜datacleaning.py
 ┃ ┣ 📜evaluation.py
 ┃ ┣ 📜gradientboosting.py
 ┃ ┣ 📜logger.py
 ┃ ┣ 📜logisticregression.py
 ┃ ┣ 📜main.py
 ┃ ┗ 📜randomforest.py
 ┣ 📜eda.ipynb
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜run.sh


## Section C - Installation and Execution
Instructions for executing pipeline - 
First, use terminal or cmd.exe to install requirements.txt in your virtual env/ VM or local machine
    $pip3 install -r requirements.txt 
    $cd to root of folder 
    $./run.sh 
Follow CLI instructions (This confirm works in both UNIX and Windows OS)

## Section D - Pipeline steps 

job.sh solely executes main.py

as such, main.py is THE main workflow. 

    Step 1) Connect to database at data/survive.db (This is not included in the submission) This is done via databaseconnect.py using sqllite3 connection

    Step 2)Database is extracted as dataframe using pandas, and a summary of the original data is provided for you via the CLI tool. 

    Step 3)Dataset is cleaned and written to csv before writing a summary of the cleaned dataset, which is provided for you via the CLI tool. To step through each specific ETL step, see eda.ipynb Task 1 Section 3

    Step 4)Pipeline from Sci Kit Learn is set up to ingest the clean data and transform it further using onehot encoding, categorical encoding and standard scaler (for numerical values) before the data is loaded into a ML model. 

    Step 5)Choose between Log Regression, Random Forest, Gradient Boosting

    Step 6)Model is trained and fitted for you automatically

    Step 7)Review Evaluation metric of your choice. 

    Step 8)Repeat steps 4-7 for other ML Models 




