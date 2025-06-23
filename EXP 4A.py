import pandas as pd

# Load your sales data CSV
df = pd.read_csv("C:\\Users\\nanthinisenthil18\\Desktop\\DEV\\EXP 4 city_sales.csv")

# Create a proper datetime column
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# Extract month name
df['MonthName'] = df['Date'].dt.month_name()

# Group by City and MonthName and sum sales
monthly_sales = df.groupby(['City', 'MonthName'])['SalesAmount'].sum().reset_index()

# Pivot table: cities as rows, months as columns
pivot_table = monthly_sales.pivot(index='City', columns='MonthName', values='SalesAmount').fillna(0)

# Add total sales per city
pivot_table['TotalSales'] = pivot_table.sum(axis=1)

# Print the pivot table
print("City-wise Monthly Sales Summary:")
print(pivot_table)

# City with highest total sales
top_city = pivot_table['TotalSales'].idxmax()
top_sales = pivot_table['TotalSales'].max()
print(f"\nCity with highest total sales: {top_city} (${top_sales:.2f})")
