# 16. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and
# contains information about the passengers who boarded the unfortunate
# Titanic ship. Write a code to check how the price of the ticket (column
# name: 'fare') for each passenger is distributed by plotting a histogram.
# Import necessary libraries
# Import necessary libraries




# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from the given CSV file
file_path = 'C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM/Titanic.csv'
titanic = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
print(titanic.head())

# Check for missing values in the dataset
print(titanic.isnull().sum())

# Set Seaborn style for the plots
sns.set(style="whitegrid")

# Plotting the distribution of 'Age' and 'Fare'
plt.figure(figsize=(12, 6))

# Age distribution
plt.subplot(1, 2, 1)
sns.histplot(titanic['Age'].dropna(), kde=True, color='blue', bins=30)
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')

# Fare distribution
plt.subplot(1, 2, 2)
sns.histplot(titanic['Fare'], kde=True, color='green', bins=30)
plt.title('Fare Distribution of Titanic Passengers')
plt.xlabel('Fare')

plt.tight_layout()
plt.show()
# Visualize the survival count based on Pclass, Sex, and Embarked
plt.figure(figsize=(12, 6))

# Pclass vs Survival
plt.subplot(1, 2, 1)
sns.countplot(x='Pclass', hue='Survived', data=titanic, palette='muted')
plt.title('Survival Count by Pclass')

# Sex vs Survival
plt.subplot(1, 2, 2)
sns.countplot(x='Sex', hue='Survived', data=titanic, palette='muted')
plt.title('Survival Count by Sex')

plt.tight_layout()
plt.show()

# Select only the numeric columns for correlation heatmap
numeric_columns = titanic.select_dtypes(include=['float64', 'int64'])

# Heatmap of correlations between numerical features
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=1)
plt.title('Correlation Heatmap of Titanic Dataset')
plt.show()

















# # Step 1: Load the Titanic dataset from the given CSV file
# titanic = pd.read_csv('C:/path_to_your_data.csv')

# # Step 2: Check the first few rows of the dataset to understand its structure
# print(titanic.head())

# # Step 3: Check for missing values in the dataset
# print(titanic.isnull().sum())

# # Step 4: Set the Seaborn plot style for clean visuals
# sns.set(style="whitegrid")

# # Step 5: Plot the Age distribution
# sns.histplot(titanic['Age'].dropna(), kde=True, color='blue', bins=30)

# # Step 6: Plot the Fare distribution
# sns.histplot(titanic['Fare'], kde=True, color='green', bins=30)

# # Step 7: Visualize survival count by Pclass
# sns.countplot(x='Pclass', hue='Survived', data=titanic)

# # Step 8: Visualize survival count by Sex
# sns.countplot(x='Sex', hue='Survived', data=titanic)

# # Step 9: Generate a heatmap for correlation between numerical columns
# sns.heatmap(titanic.corr(), annot=True, cmap='coolwarm', fmt='.2f')
