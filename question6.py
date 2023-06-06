import pandas as pd
import requests

# Step 1: Download the data from the provided link
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Step 2: Process the data and convert it into a pandas DataFrame
pokemon_list = data["pokemon"]

# Create empty lists to store the extracted attributes
spawn_rate_less_than_5 = []
less_than_4_weaknesses = []
no_multipliers = []
less_than_2_evolutions = []
spawn_time_less_than_300 = []
more_than_two_capabilities = []

for pokemon in pokemon_list:
    # Get all Pokemons whose spawn rate is less than 5%
    if pokemon.get("spawn_chance", 0) < 5:
        spawn_rate_less_than_5.append(pokemon)

    # Get all Pokemons that have less than 4 weaknesses
    if len(pokemon.get("weaknesses", [])) < 4:
        less_than_4_weaknesses.append(pokemon)

    # Get all Pokemons that have no multipliers at all
    if not pokemon.get("multipliers"):
        no_multipliers.append(pokemon)

    # Get all Pokemons that do not have more than 2 evolutions
    if len(pokemon.get("next_evolution", [])) + len(pokemon.get("prev_evolution", [])) <= 2:
        less_than_2_evolutions.append(pokemon)

    # Get all Pokemons whose spawn time is less than 300 seconds
    spawn_time = pokemon.get("spawn_time", "")
    if spawn_time and int(spawn_time.split(":")[0]) * 60 + int(spawn_time.split(":")[1]) < 300:
        spawn_time_less_than_300.append(pokemon)

    # Get all Pokemon who have more than two types of capabilities
    if len(pokemon.get("type", [])) > 2:
        more_than_two_capabilities.append(pokemon)

# Print the analysis results
print("Pokemons whose spawn rate is less than 5%:")
for pokemon in spawn_rate_less_than_5:
    print(pokemon["name"])

print("\nPokemons that have less than 4 weaknesses:")
for pokemon in less_than_4_weaknesses:
    print(pokemon["name"])

print("\nPokemons that have no multipliers at all:")
for pokemon in no_multipliers:
    print(pokemon["name"])

print("\nPokemons that do not have more than 2 evolutions:")
for pokemon in less_than_2_evolutions:
    print(pokemon["name"])

print("\nPokemons whose spawn time is less than 300 seconds:")
for pokemon in spawn_time_less_than_300:
    print(pokemon["name"])

print("\nPokemon who have more than two types of capabilities:")
for pokemon in more_than_two_capabilities:
    print(pokemon["name"])
