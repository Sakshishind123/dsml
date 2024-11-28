import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
csv_file = "C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM/IRIS.csv"
iris_data = pd.read_csv(csv_file)

# Inspect the data
print(iris_data.describe())  # Descriptive statistics for all numerical features

# Select numerical features
numeric_features = iris_data.columns[:-1]  # Exclude the 'species' column

# Create box plots for each feature
for feature in numeric_features:
    # Box Plot
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=iris_data[feature])
    plt.title(f"Box Plot of {feature}")
    plt.xlabel(feature)
    plt.show()
    
    # Distribution (Histogram with KDE)
    plt.figure(figsize=(6, 4))
    sns.histplot(iris_data[feature], kde=True, bins=15, color='blue')
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()
    
    # Identify Outliers using the IQR Method
    Q1 = iris_data[feature].quantile(0.25)  # First quartile
    Q3 = iris_data[feature].quantile(0.75)  # Third quartile
    IQR = Q3 - Q1  # Interquartile range
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Outliers
    outliers = iris_data[(iris_data[feature] < lower_bound) | (iris_data[feature] > upper_bound)]
    print(f"Feature: {feature}")
    print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
    print(f"Number of Outliers: {len(outliers)}")
    if not outliers.empty:
        print("Outlier values:")
        print(outliers[feature].values)
    else:
        print("No outliers detected.")
    print("\n")
