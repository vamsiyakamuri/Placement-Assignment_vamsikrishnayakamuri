import requests
import matplotlib.pyplot as plt


# Step 1: Download the data from the API link
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()

# Step 2: Extract the required data attributes
show_id = data["id"]
show_url = data["url"]
show_name = data["name"]
episodes = data["_embedded"]["episodes"]

# Process each episode and extract the required attributes
episode_data = []
for episode in episodes:
    episode_id = episode["id"]
    episode_url = episode["url"]
    episode_season = episode["season"]
    episode_number = episode["number"]
    episode_type = episode["type"]
    episode_airdate = episode["airdate"]
    episode_airtime = episode["airtime"]
    episode_runtime = episode["runtime"]
    episode_average_rating = episode["rating"]["average"]
    episode_summary = episode["summary"].strip("<p>").strip("</p>")
    episode_image_medium = episode["image"]["medium"]
    episode_image_original = episode["image"]["original"]

    episode_info = {
        "id": episode_id,
        "url": episode_url,
        "name": show_name,
        "season": episode_season,
        "number": episode_number,
        "type": episode_type,
        "airdate": episode_airdate,
        "airtime": episode_airtime,
        "runtime": episode_runtime,
        "average_rating": episode_average_rating,
        "summary": episode_summary,
        "image_medium": episode_image_medium,
        "image_original": episode_image_original
    }
    episode_data.append(episode_info)

# Step 3: Print or process the extracted episode data as per the analysis requirements

# 1. Get all the overall ratings for each season and compare the ratings for all the seasons
season_ratings = {}
for episode in episode_data:
    season = episode["season"]
    rating = episode["average_rating"]
    if season in season_ratings:
        season_ratings[season].append(rating)
    else:
        season_ratings[season] = [rating]

# 2. Get all the episode names whose average rating is more than 8 for every season
highly_rated_episodes = []
for episode in episode_data:
    rating = episode["average_rating"]
    if rating > 8:
        highly_rated_episodes.append(episode["name"])

# 3. Get all the episode names that aired before May 2019
episodes_before_may_2019 = []
for episode in episode_data:
    airdate = episode["airdate"]
    if airdate < "2019-05-01":
        episodes_before_may_2019.append(episode["name"])

# 4. Get the episode name from each season with the highest and lowest rating
season_highest_ratings = {}
season_lowest_ratings = {}
for episode in episode_data:
    season = episode["season"]
    rating = episode["average_rating"]
    episode_name = episode["name"]
    if season in season_highest_ratings:
        if rating > season_highest_ratings[season][1]:
            season_highest_ratings[season] = (episode_name, rating)
        if rating < season_lowest_ratings[season][1]:
            season_lowest_ratings[season] = (episode_name, rating)
    else:
        season_highest_ratings[season] = (episode_name, rating)
        season_lowest_ratings[season] = (episode_name, rating)

# 5. Get the summary for the most popular (highest ratings) episode in every season
most_popular_episodes = {}
for episode in episode_data:
    season = episode["season"]
    rating = episode["average_rating"]
    summary = episode["summary"]
    if season in most_popular_episodes:
        if rating > most_popular_episodes[season][1]:
            most_popular_episodes[season] = (episode["name"], rating, summary)
    else:
        most_popular_episodes[season] = (episode["name"], rating, summary)

# Step 4: Perform any necessary analysis and visualization using the extracted data

# Example: Plotting season ratings
import matplotlib.pyplot as plt

seasons = list(season_ratings.keys())
ratings = [sum(ratings) / len(ratings) for ratings in season_ratings.values()]

plt.bar(seasons, ratings)
plt.xlabel("Season")
plt.ylabel("Average Rating")
plt.title("Average Ratings for Each Season")
plt.show()
