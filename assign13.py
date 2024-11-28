# Use the covid_vaccine_statewise.csv dataset and perform the following analytics.

# Describe the dataset
# Number of persons state wise vaccinated for first dose in India
# Number of persons state wise vaccinated for second dose in India


import pandas as pd
csv_file = "C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM/Covid Vaccine Statewise.csv"
covid_data = pd.read_csv(csv_file)
covid_data.head()
# a. Describe the dataset
print("Dataset Description:")
print(covid_data.describe())



# b. Number of persons state-wise vaccinated for the first dose in India
# 'First Dose Administered' is the relevant column for the first dose
first_dose_vaccinated = covid_data.groupby('State')['First Dose Administered'].sum()
print("\nNumber of persons state-wise vaccinated for first dose:")
print(first_dose_vaccinated)


# c. Number of persons state-wise vaccinated for the second dose in India
# 'Second Dose Administered' is the relevant column for the second dose
second_dose_vaccinated = covid_data.groupby('State')['Second Dose Administered'].sum()

print("\nNumber of persons state-wise vaccinated for second dose:")
print(second_dose_vaccinated)

