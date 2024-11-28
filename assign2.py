import pandas as pd

# Load the dataset
file_path = 'C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM/Telecom Churn (1).csv'  # Update path if needed
df = pd.read_csv(file_path)

# Select numerical columns
num_col = df.select_dtypes(include=['float64', 'int64']).columns

# Calculate summary statistics
summary = {
    'Min': df[num_col].min(),
    'Max': df[num_col].max(),
    'Mean': df[num_col].mean(),
    'Range': df[num_col].max() - df[num_col].min(),
    'Std Dev': df[num_col].std(),
    'Variance': df[num_col].var(),
    '25th': df[num_col].quantile(0.25),
    '50th (Median)': df[num_col].quantile(0.5),
    '75th': df[num_col].quantile(0.75)
}

# Convert to DataFrame for readability
summary_df = pd.DataFrame(summary)

# Print summary
print(summary_df)
