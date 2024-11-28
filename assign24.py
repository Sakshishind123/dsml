import pandas as pd

# Load the dataset
file_path = 'C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM/IRIS.csv'
data = pd.read_csv(file_path)

# 1. Counting unique values of each column
unique_values = data.nunique()
print("Unique values in each column:")
print(unique_values)

# 2. Format (data type) of each column
column_data_types = data.dtypes
print("\nData types of each column:")
print(column_data_types)

# 3. Identifying missing values
missing_values = data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# 4. Fill missing values in numeric columns
# Select only numeric columns to apply mean fill
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

# Fill missing values in categorical columns with a placeholder
categorical_columns = data.select_dtypes(include=['object']).columns
data[categorical_columns] = data[categorical_columns].fillna('Unknown')

# Print the updated dataset after filling missing values
print("\nDataset after filling missing values:")
print(data.head())
