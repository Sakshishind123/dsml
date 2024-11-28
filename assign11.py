import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_data = pd.read_csv('IRIS.csv')  # Ensure 'IRIS.csv' is in the working directory

# Question 11.1: List down features and their types
print("Features and their types:")
print(iris_data.dtypes)

# Question 11.2: Create histograms for each feature
numeric_features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

plt.figure(figsize=(12, 8))
for i, feature in enumerate(numeric_features, 1):
    plt.subplot(2, 2, i)
    plt.hist(iris_data[feature], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
