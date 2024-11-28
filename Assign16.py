# Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and
# contains information about the passengers who boarded the unfortunate
# Titanic ship. Write a code to check how the price of the ticket (column
# name: 'fare') for each passenger is distributed by plotting a histogram.










# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn's inbuilt datasets
titanic = sns.load_dataset('titanic')

# Set the size of the plot
plt.figure(figsize=(10, 6))

# Plot the histogram of the 'Fare' column
sns.histplot(titanic['fare'], kde=True, color='blue', bins=30)

# Set title and labels
plt.title('Distribution of Ticket Prices (Fare) for Titanic Passengers')
plt.xlabel('Fare')
plt.ylabel('Frequency')

# Show the plot
plt.show()
