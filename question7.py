import pandas as pd
import requests

# Step 1: Download the data from the provided link
url = "https://data.nasa.gov/resource/y77d-th95.json"
response = requests.get(url)
data = response.json()

# Step 2: Process the data and convert it into a pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Drop rows with missing values in the 'year' column
df = df.dropna(subset=['year'])

# Step 4: Convert the 'year' column to integer
df['year'] = df['year'].str[:4].astype(int)

# Step 5: Save the data as a CSV file
csv_filename = "earth_meteorites.csv"
df.to_csv(csv_filename, index=False)

# Analysis: Insights to be drawn

# Get all the Earth meteorites that fell before the year 2000
meteorites_before_2000 = df[df['year'] < 2000]

# Get all the Earth meteorites coordinates that fell before the year 1970
meteorites_coordinates_before_1970 = df[df['year'] < 1970][['reclat', 'reclong']]

# Assuming that the mass of the Earth meteorites was in kg,
# get all those whose mass was more than 10000 kg
mass_more_than_10000kg = df[df['mass'].astype(float) > 10000]

# Print the insights
print("Earth meteorites that fell before the year 2000:")
print(meteorites_before_2000)

print("\nEarth meteorites coordinates that fell before the year 1970:")
print(meteorites_coordinates_before_1970)

print("\nEarth meteorites with mass more than 10000 kg:")
print(mass_more_than_10000kg)
