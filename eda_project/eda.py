import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
print("Current Directory:", os.getcwd())


# Load the dataset
df = pd.read_csv(r'C:\Users\mfshi\eda_project\data\titanic.csv')


# Show first few rows
print(df.head())

# Show basic info
print(df.info())

# Show summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Plot: Histogram of a column
sns.histplot(df['Age'])  # Replace 'Age' with a column in your dataset
plt.show()

# Plot: Correlation heatmap
sns.heatmap(df.corr(), annot=True)
plt.show()
