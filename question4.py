import requests
import csv

# Download data from the provided link
url = "https://data.nasa.gov/resource/y77d-th95.json"
response = requests.get(url)
data = response.json()

# Define the desired output data attributes
output_data = []
output_data_attributes = [
    "name", "id", "nametype", "recclass", "mass", "year", "reclat", "reclong"
]

# Convert data into the proper structure
for item in data:
    output_item = {}
    for attribute in output_data_attributes:
        if attribute in item:
            output_item[attribute] = item[attribute]
        else:
            output_item[attribute] = None
    output_data.append(output_item)

# Save the data as a CSV file
output_file = "meteorite_data.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=output_data_attributes)
    writer.writeheader()
    writer.writerows(output_data)

print("Data has been converted and saved to", output_file)
