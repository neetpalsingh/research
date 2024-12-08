import pandas as pd 

# Load the dataset
df = pd.read_csv('/neetpal/car_dataset.csv')

# Describe
print(df.describe())
# Shape
print(f"Shape of the dataset: {df.shape}") 
# Columns
print(f"Columns in the dataset: {df.columns}") 

# Head
print("First five rows of the dataset:") 
print(df.head())

# Check for missing values
print("Missing values in each column:") 
print(df.isnull().sum())

# Check for unique values
print("Number of unique values in each column:") 
print(df.nunique())
