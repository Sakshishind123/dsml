import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'House Data.csv'  # Adjust the path if needed
data = pd.read_csv('C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM\House Data.csv')

# Preprocessing: Convert 'price' and 'GrossSquareMeters' to numeric
data['price'] = data['price'].str.replace(r'[^\d]', '', regex=True).astype(float)
data['GrossSquareMeters'] = data['GrossSquareMeters'].str.replace(r'[^\d]', '', regex=True).astype(float)

# Identify numerical columns
numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns

# Compute Standard Deviation, Variance, and Percentiles
for col in numerical_columns:
    print(f"\nStatistics for {col}:")
    print(f"  Standard Deviation: {data[col].std()}")
    print(f"  Variance: {data[col].var()}")
    print(f"  25th Percentile: {data[col].quantile(0.25)}")
    print(f"  50th Percentile (Median): {data[col].median()}")
    print(f"  75th Percentile: {data[col].quantile(0.75)}")

# Create Histograms
for col in numerical_columns:
    plt.figure()
    plt.hist(data[col].dropna(), bins=30, edgecolor='k')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()





