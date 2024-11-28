import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Data Preparation
data = {
    "Age": ["<21", "<21", "21-35", ">35", ">35", ">35", "21-35", "<21", "<21", ">35", "<21", "21-35", "21-35", ">35"],
    "Income": ["High", "High", "High", "Medium", "Low", "Low", "Low", "Medium", "Low", "Medium", "Medium", "Medium", "High", "Medium"],
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Female", "Female", "Female", "Male", "Female", "Male"],
    "Marital_Status": ["Single", "Married", "Single", "Single", "Single", "Married", "Married", "Single", "Married", "Single", "Married", "Married", "Single", "Married"],
    "Buys": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

# Create a LabelEncoder for each column
encoders = {col: LabelEncoder() for col in df.columns}

# Encode the data
for col, encoder in encoders.items():
    df[col] = encoder.fit_transform(df[col])

# Split features and target
X = df[["Age", "Income", "Gender", "Marital_Status"]]
y = df["Buys"]

# Train Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Test data: [Age < 21, Income = Low, Gender = Female, Marital Status = Married]
test_data = {
    "Age": ["<21"],
    "Income": ["Low"],
    "Gender": ["Female"],
    "Marital_Status": ["Married"]
}

# Encode the test data using the same encoders
test_data_encoded = {col: encoders[col].transform(test_data[col])[0] for col in test_data}
test_df = pd.DataFrame([test_data_encoded])

# Predict
prediction = clf.predict(test_df)
print("Prediction (0 = No, 1 = Yes):", prediction[0])

# Decode prediction
decoded_prediction = encoders["Buys"].inverse_transform(prediction)
print("Final Decision:", decoded_prediction[0])
















# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, export_text

# # Create the dataset
# data = {
#     'Age': ['<21', '<21', '21-35', '>35', '>35', '>35', '21-35', '<21', '<21', '>35', '<21', '21-35', '21-35', '>35'],
#     'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'High', 'Medium'],
#     'Gender': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Male'],
#     'Marital Status': ['Single', 'Married', 'Single', 'Single', 'Single', 'Married', 'Married', 'Single', 'Married', 'Single', 'Married', 'Married', 'Single', 'Married'],
#     'Buys': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
# }

# # Convert the dataset to a DataFrame
# df = pd.DataFrame(data)

# # Encode categorical variables
# df_encoded = pd.get_dummies(df, columns=['Age', 'Income', 'Gender', 'Marital Status'], drop_first=True)

# # Split features and target
# X = df_encoded.drop(columns=['Buys'])
# y = df['Buys'].apply(lambda x: 1 if x == 'Yes' else 0)

# # Train the Decision Tree Classifier
# clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
# clf.fit(X, y)

# # Display the Decision Tree
# tree_rules = export_text(clf, feature_names=list(X.columns))
# print("Decision Tree Rules:")
# print(tree_rules)

# # Create test data dynamically with all features set to 0
# test_data = pd.DataFrame([0] * len(X.columns), index=X.columns).T

# # Update specific features in test data
# test_data['Age_<21'] = 1
# test_data['Income_Low'] = 1
# test_data['Gender_Male'] = 0
# test_data['Marital Status_Single'] = 0  # Married implies Single = 0

# # Predict for the test data
# prediction = clf.predict(test_data)
# result = 'Yes' if prediction[0] == 1 else 'No'

# print("\nDecision for the test data [Age < 21, Income = Low, Gender = Female, Marital Status = Married]:", result)





