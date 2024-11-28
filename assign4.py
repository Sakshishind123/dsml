# Load the dataset manually (without libraries)
data = []
with open('Lipstick.csv', 'r') as file:
    for line in file:
        data.append(line.strip().split(','))

# Extract headers and rows
headers = data[0]
rows = data[1:]

# Define functions for Decision Tree
def entropy(data, target_col):
    from math import log2
    total = len(data)
    target_values = [row[target_col] for row in data]
    value_counts = {val: target_values.count(val) for val in set(target_values)}
    return -sum((count/total) * log2(count/total) for count in value_counts.values())

def information_gain(data, split_col, target_col):
    total_entropy = entropy(data, target_col)
    unique_values = set(row[split_col] for row in data)
    weighted_entropy = 0
    for value in unique_values:
        subset = [row for row in data if row[split_col] == value]
        weighted_entropy += (len(subset)/len(data)) * entropy(subset, target_col)
    return total_entropy - weighted_entropy

def find_best_split(data, target_col):
    best_gain = 0
    best_col = None
    for col in range(len(data[0])):
        if col == target_col:
            continue
        gain = information_gain(data, col, target_col)
        if gain > best_gain:
            best_gain = gain
            best_col = col
    return best_col

def build_tree(data, headers, target_col):
    if len(set(row[target_col] for row in data)) == 1:
        return data[0][target_col]
    if len(data[0]) == 1:
        return max(set(row[target_col] for row in data), key=lambda x: [row[target_col] for row in data].count(x))
    split_col = find_best_split(data, target_col)
    tree = {headers[split_col]: {}}
    for value in set(row[split_col] for row in data):
        subset = [row for row in data if row[split_col] == value]
        tree[headers[split_col]][value] = build_tree(subset, headers, target_col)
    return tree

# Build the decision tree
target_col = headers.index('Buys')  # Replace 'Buys' with the target column name
decision_tree = build_tree(rows, headers, target_col)

# Print the decision tree
print("Decision Tree:")
print(decision_tree)
