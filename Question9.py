import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the provided link
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Get all the cars and their types that do not qualify for clean alternative fuel vehicle
# Filter the DataFrame to include only cars that do not qualify for clean alternative fuel vehicles
non_cafv_cars = df[df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] != 'Qualified']

# Select the 'Make' and 'Model' columns for the filtered cars
non_cafv_car_types = non_cafv_cars[['Make', 'Model']]

# Check if the DataFrame is empty
if non_cafv_car_types.empty:
    print("No cars found that do not qualify for clean alternative fuel vehicles.")
else:
    # Print the result
    print(non_cafv_car_types)


# Filter the DataFrame to include only TESLA cars made in Bothell City
tesla_bothell_cars = df[(df['Make'] == 'TESLA') & (df['City'] == 'BOTHELL')]

# Select the 'Model Year' and 'Model' columns for the filtered cars
tesla_bothell_info = tesla_bothell_cars[['Model Year', 'Model']]

# Save the output to a text file
output_file = 'tesla_bothell_info.txt'
tesla_bothell_info.to_csv(output_file, sep='\t', index=False)

print("Output saved to:", output_file)


# Get all the cars that have an electric range of more than 100 and were made after 2015
electric_range_cars = df[(df['Electric Range'] > 100) & (df['Model Year'] > 2015)]
electric_range_cars_info = electric_range_cars[['Make', 'Model', 'Electric Range', 'Model Year']]
print("Cars with electric range > 100 and made after 2015:")
print(electric_range_cars_info)

# Draw plots to show the distribution between city and electric vehicle type
city_counts = df['City'].value_counts().head(10)
plt.figure(figsize=(10, 6))
city_counts.plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Count')
plt.title('Distribution of Electric Vehicle Types by City')
plt.show()
