import pandas as pd

# Load dataset (assumed to contain Department and Productivity_Score)
df = pd.read_csv("C:\\Users\\nanthinisenthil18\\Desktop\\DEV\\EXP 4B department_productivity.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Drop rows where critical columns are missing
df = df.dropna(subset=['Department', 'Productivity_Score'])

# Ensure productivity score is numeric
df['Productivity_Score'] = pd.to_numeric(df['Productivity_Score'], errors='coerce')
df = df.dropna(subset=['Productivity_Score'])

# Group by department and calculate average productivity
dept_productivity = df.groupby('Department')['Productivity_Score'].mean().reset_index()

# Pivot table for clarity (optional here, since only one value column)
pivot_table = dept_productivity.pivot_table(values='Productivity_Score', index='Department')

# Identify department with highest average productivity
max_dept = pivot_table['Productivity_Score'].idxmax()
max_score = pivot_table['Productivity_Score'].max()

# Print summary
print("\n📈 Department-wise Average Productivity Scores:\n")
print(pivot_table)

print(f"\n🏆 Highest Average Productivity:\n{max_dept} → {max_score:.2f} points")
