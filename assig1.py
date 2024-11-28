import pandas as pd

# Load Titanic dataset from CSV or Excel
# titanic_csv_path = "titanic.csv"  # Update this with your file path
 

# Reading CSV and Excel files
df_csv = pd.read_csv('C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM/Titanic.csv')


# Display first few rows of the dataset
print("CSV Data Preview:")
print(df_csv.head())


# Indexing and Selecting Data
# Select a column (e.g., 'Age')
print("\nSelected 'Age' column from CSV:")
print(df_csv['Age'].head())

# Select multiple columns (e.g., 'Name', 'Age', 'Survived')
print("\nSelected 'Name', 'Age', and 'Survived' columns from CSV:")
print(df_csv[['Name', 'Age', 'Survived']].head())

# Select rows where Age > 60
print("\nPassengers older than 60:")
print(df_csv[df_csv['Age'] > 60].head())

# Sort Data
# Sort by 'Age'
print("\nData sorted by 'Age' in ascending order:")
print(df_csv.sort_values(by='Age').head())

# Sort by 'Age' and 'Pclass'
print("\nData sorted by 'Age' (ascending) and 'Pclass' (descending):")
print(df_csv.sort_values(by=['Age', 'Pclass'], ascending=[True, False]).head())

# Describe the Data
print("\nSummary statistics for numerical columns:")
print(df_csv.describe())

# Check data types of each column
print("\nData types of each column:")
print(df_csv.dtypes)


