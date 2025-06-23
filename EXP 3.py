import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("🌡️ NumPy Temperature Analysis:")

# NumPy Array: Weekly temperature (in Celsius)
temps = np.array([28, 30, 27, 29, 31, 33, 32])
print("Temperatures for the week (°C):", temps)

# Convert to Fahrenheit
fahrenheit = (temps * 9/5) + 32
print("Temperatures in Fahrenheit:", fahrenheit)

# Temperature differences from average
avg_temp = np.mean(temps)
print("Average Temp (°C):", avg_temp)
print("Deviation from average:", temps - avg_temp)

print("\n📋 Pandas Weather DataFrame Operations:")

weather_data = {
    'City': ['Chennai', 'Bangalore', 'Delhi', 'Mumbai', 'Hyderabad'],
    'MaxTemp': [35, 31, 40, 34, 36],
    'MinTemp': [27, 22, 28, 26, 25]
}

df = pd.DataFrame(weather_data)
print("\nWeather DataFrame:")
print(df)

# Add new column: Temperature Range
df['TempRange'] = df['MaxTemp'] - df['MinTemp']
print("\nWith Temperature Range:")
print(df)

print("\n📊 Generating Plots...")

# Bar chart for MaxTemp
plt.figure(figsize=(8, 4))
plt.bar(df['City'], df['MaxTemp'], color='tomato')
plt.title("Maximum Temperatures by City")
plt.xlabel("City")
plt.ylabel("Max Temperature (°C)")
plt.tight_layout()
plt.show()

# Line chart for Max and Min temperatures
plt.figure(figsize=(8, 4))
plt.plot(df['City'], df['MaxTemp'], marker='o', label='Max Temp')
plt.plot(df['City'], df['MinTemp'], marker='^', label='Min Temp')
plt.title("Temperature Trends by City")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
