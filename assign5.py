
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text


csv_file = r'C:\Users\saksh\OneDrive\Desktop\DSML PRACT. EXAM\Lipstick.csv'

data = pd.read_csv(csv_file)
data.head()
data = data.drop(columns=["Id"])

# Convert categorical data to numeric using one-hot encoding
X= pd.get_dummies(data.drop(columns=["Buys"]))
y= data["Buys"].apply(lambda x: 1 if x == "Yes" else 0) 
 # Encode target (Yes=1, No=0)


# Train a Decision Tree Classifier
dtc = DecisionTreeClassifier(criterion="gini")
dtc.fit(X, y)
#  fit() trains the model on your data.

# Print the decision tree rules
feature_names = X.columns
decision_tree_rules = export_text(dtc, feature_names=list(feature_names))
print("Decision Tree Rules:\n")
print(decision_tree_rules)

# The export_text() function provides a readable version
# of the decision tree, showing how it splits data.

# Test data: [Age < 21, Income = Low, Gender = Female, Marital Status = Married]
test_data = pd.DataFrame({
    "Age_<21": [1],
    "Age_21-35": [0],
    "Age_>35": [0],
    "Income_High": [0],
    "Income_Low": [0],
    "Income_Medium": [1],
    "Gender_Female": [1],
    "Gender_Male": [0],
    "Ms_Married": [1],
    "Ms_Single": [0]
})

# Align test_data columns with training data
test_data = test_data.reindex(columns=X.columns, fill_value=0)

# Make prediction
prediction = dtc.predict(test_data)
print("\nPrediction for the test data (Buys):", "Yes" if prediction[0] == 1 else "No")



