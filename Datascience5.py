import pandas as pd

# Load the dataset
df = pd.read_csv('US_Accidents_Dec20.csv')

# Display the first few rows and inspect the columns
print(df.head())
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values in important columns (adjust as necessary)
df = df.dropna(subset=['Start_Time', 'Weather_Condition', 'State', 'Visibility(mi)', 'Temperature(F)', 'Severity'])

# Convert Start_Time to datetime format
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Extract hour of day from Start_Time
df['Hour'] = df['Start_Time'].dt.hour

import matplotlib.pyplot as plt
import seaborn as sns

# Visualize accident count by severity
plt.figure(figsize=(10, 6))
sns.countplot(x='Severity', data=df, palette='viridis')
plt.title('Accident Count by Severity')
plt.xlabel('Severity')
plt.ylabel('Count')
plt.show()

# Visualize accidents by weather condition
plt.figure(figsize=(12, 6))
sns.countplot(y='Weather_Condition', data=df, order=df['Weather_Condition'].value_counts().index[:10], palette='coolwarm')
plt.title('Accidents by Weather Condition (Top 10)')
plt.xlabel('Count')
plt.ylabel('Weather Condition')
plt.show()

# Visualize accidents by hour of day
plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, palette='magma')
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Count')
plt.show()

import folium
from folium.plugins import HeatMap

# Filter out accidents with exact location information (latitude and longitude)
df = df.dropna(subset=['Start_Lat', 'Start_Lng'])

# Sample data for faster visualization (adjust as needed)
sample_df = df.sample(10000)  # You can increase or decrease the sample size for better visualization

# Create a map centered around the USA
accident_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Plot heatmap of accidents
HeatMap(data=sample_df[['Start_Lat', 'Start_Lng']].values.tolist(), radius=10).add_to(accident_map)

# Display the map
accident_map.save('accident_hotspots.html')  # Save the map to an HTML file
accident_map

# Visualize accidents by contributing factors (e.g., junction type, road type)
plt.figure(figsize=(12, 6))
sns.countplot(y='Junction_Type', data=df, order=df['Junction_Type'].value_counts().index[:5], palette='Set2')
plt.title('Accidents by Junction Type (Top 5)')
plt.xlabel('Count')
plt.ylabel('Junction Type')
plt.show()
