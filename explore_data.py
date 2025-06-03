import pandas as pd

# Load the data
df = pd.read_csv("netflix_titles.csv")

# Display first few rows
print(df.head())

# Basic info
print(df.info())

# Missing values
print(df.isnull().sum())
