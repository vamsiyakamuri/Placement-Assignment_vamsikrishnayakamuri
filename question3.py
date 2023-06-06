import pandas as pd
import requests
from requests.exceptions import ConnectTimeout

# Step 1: Download the data from the provided link
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

max_retries = 3  # Maximum number of retries
retry_count = 0

while retry_count < max_retries:
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        break  # Break out of the loop if download is successful
    except ConnectTimeout:
        retry_count += 1
        print(f"Connection timeout occurred. Retrying... (Attempt {retry_count}/{max_retries})")

if retry_count == max_retries:
    print("Maximum retries exceeded. Unable to download the data.")
    exit()

# Step 2: Process the data and convert it into a pandas DataFrame
pokemon_list = data["pokemon"]

# Rest of the code remains the same...

# Create a pandas DataFrame from the extracted attributes
df = pd.DataFrame({
    # Attribute columns...
})

# Rest of the code remains the same...

# Step 3: Save the DataFrame as an Excel file
output_file = "pokemon_data.xlsx"
df.to_excel(output_file, index=False)
print("Data saved successfully to", output_file)
