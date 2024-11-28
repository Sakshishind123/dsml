import pandas as pd

# Load the Iris dataset
iris_data = pd.read_csv('IRIS.csv')  # Make sure the correct path to the file is provided

# Question 19: Statistical details for each species
species_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

for species in species_list:
    print(f"\nStatistical Details for {species}:")
    species_data = iris_data[iris_data['species'] == species]
    print(species_data.describe())  # Basic statistical details
