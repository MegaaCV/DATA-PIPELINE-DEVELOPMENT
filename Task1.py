# Task 1 : Automated ETL pipeline for a dataset

# Importing necessary libraries

import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.impute import SimpleImputer
import os

# Extracting the dataset

def extract_data(path):
    # Prompt the user for CSV file path and load the dataset

    while not os.path.isfile(path) or not path.endswith(".csv"):
        print("Invalid file path or invalid file format")
        path=input("Try again:").strip()
    print(f"Extracting data from :{path}")
    return pd.read_csv(path),path

# Transforming the dataset

def preprocess_data(df):
    print("Transforming the dataset...")
    # identify numeric and categorical columns
    numeric_col=df.select_dtypes(include='number').columns
    categorical_col=df.select_dtypes(include='object').columns

    # Impute missing values
    num_imputer=SimpleImputer(strategy='median')
    df[numeric_col]=num_imputer.fit_transform(df[numeric_col])
    catt_imputer=SimpleImputer(strategy='constant',fill_value='unknown')
    df[categorical_col]=catt_imputer.fit_transform(df[categorical_col])

    # Encoding of categorical columns
    for col in categorical_col:
        le=LabelEncoder()
        df[col]=le.fit_transform(df[col])

    # Scale numerical columns

    scaler=StandardScaler()
    df[numeric_col]=scaler.fit_transform(df[numeric_col])

    print("Data transformation completed.")
    return df

# Save the cleaned dataset in a new name in same folder

def save_cleaned_data(df,original_path):
    directory=os.path.dirname(original_path)
    cleaned_path=os.path.join(directory,"cleaned_data.csv")
    df.to_csv(cleaned_path,index=False)
    print(f"Cleaned data is saved at {cleaned_path}")

#Orchestrating the ETL pipeline

def etl_pipeline():
    print("Welcome to the automated ETL pipeline")
    path=input("Please enter the path of your CSV file(CSV format):").strip()
    df,path=extract_data(path)
    cleaned_df=preprocess_data(df)
    save_cleaned_data(cleaned_df,path)
    print("The ETL pipeline has been successfully completed.")

if __name__=="__main__":
    etl_pipeline()
# The code is completed

     



