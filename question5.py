import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

# Download data from the API link
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()

# Extract desired data attributes with proper formatting
show_id = data["id"]
show_url = data["url"]
show_name = data["name"]

episodes = data["_embedded"]["episodes"]
episode_data = []

for episode in episodes:
    episode_number = episode["number"]
    episode_season = episode["season"]
    episode_type = episode["type"]
    episode_airdate = episode["airdate"]
    episode_airtime = episode["airtime"]
    episode_runtime = episode["runtime"]
    episode_rating = episode["rating"]["average"]
    episode_summary = BeautifulSoup(episode["summary"], "html.parser").get_text()
    episode_image_medium = episode["image"]["medium"]
    episode_image_original = episode["image"]["original"]

    episode_data.append({
        "id": show_id,
        "url": show_url,
        "name": show_name,
        "season": episode_season,
        "number": episode_number,
        "type": episode_type,
        "airdate": episode_airdate,
        "airtime": episode_airtime,
        "runtime": episode_runtime,
        "average_rating": episode_rating,
        "summary": episode_summary,
        "medium_image_link": episode_image_medium,
        "original_image_link": episode_image_original
    })

# Save the extracted data to a structured format (e.g., DataFrame, CSV)
df = pd.DataFrame(episode_data)

# Save the DataFrame to a CSV file
output_file = "episode_data.csv"
df.to_csv(output_file, index=False)

print("Data has been extracted and saved to", output_file)
