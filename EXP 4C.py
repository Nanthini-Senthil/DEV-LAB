import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Show basic info
print("📊 Titanic Dataset Summary:")
print(titanic.info())

# Drop rows with missing 'age' or 'class'
titanic_clean = titanic.dropna(subset=['age', 'class'])

# ✅ Group by class and sex with observed=True to avoid future warning
grouped = titanic_clean.groupby(['class', 'sex'], observed=True)['age'].mean().reset_index()
print("\n👥 Average Age by Class and Gender:")
print(grouped)

# 📊 Bar Plot: Average Age by Class and Gender
plt.figure(figsize=(8, 5))
sns.barplot(x='class', y='age', hue='sex', data=grouped, palette='pastel')
plt.title("Average Passenger Age by Class and Gender")
plt.ylabel("Average Age")
plt.xlabel("Passenger Class")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 🧍‍♂️ Countplot: Survival by Gender
plt.figure(figsize=(6, 4))
sns.countplot(x='sex', hue='survived', data=titanic, palette='Set2')
plt.title("Survival Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.tight_layout()
plt.show()
