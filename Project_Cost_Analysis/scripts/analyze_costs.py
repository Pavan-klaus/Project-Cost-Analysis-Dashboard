import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../data/warehouse_projects_data.csv')

# Preview
print("Dataset Preview:\n", df.head())
print("\nTotal Projects:", len(df))

# Ensure Total Cost and Profit columns exist
if 'Total Cost' not in df.columns:
    df['Total Cost'] = df['Material Cost'] + df['Labor Cost'] + df['Equipment Cost']

# Key insights
print("\nAverage Total Cost per Project: ₹", round(df['Total Cost'].mean(), 2))
print("Average Profit Margin (%):", round(df['Profit Margin (%)'].mean(), 2))

# Top 5 profitable projects
top_profit = df.sort_values(by='Profit Value', ascending=False).head(5)
print("\nTop 5 Profitable Projects:\n", top_profit[['Project Name', 'Client', 'Profit Value']])

# Visualization 1: Total Cost per Project
plt.figure(figsize=(10,6))
plt.bar(df['Project Name'], df['Total Cost'])
plt.title('Total Project Cost Comparison')
plt.xlabel('Project Name')
plt.ylabel('Total Cost (₹)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Visualization 2: Profit Margin per Project
plt.figure(figsize=(10,6))
plt.bar(df['Project Name'], df['Profit Margin (%)'], color='orange')
plt.title('Profit Margin per Project')
plt.xlabel('Project Name')
plt.ylabel('Profit Margin (%)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Save cleaned data
df.to_csv('../data/cleaned_warehouse_projects.csv', index=False)
print("\nCleaned data saved as cleaned_warehouse_projects.csv")
