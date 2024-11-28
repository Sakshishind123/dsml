# Given values
TP = 90  # True Positives
FP = 140 # False Positives
FN = 210 # False Negatives
TN = 9560 # True Negatives
Total = 10000 # Total instances

# Accuracy
accuracy = (TP + TN) / Total

# Error Rate
error_rate = (FP + FN) / Total

# Precision (for class "Yes")
precision = TP / (TP + FP)

# Recall (for class "Yes")
recall = TP / (TP + FN)

print(f"Accuracy: {accuracy:.4f}")
print(f"Error Rate: {error_rate:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")