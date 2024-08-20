import requests

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    return response.json()

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemon_data:
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Name: {name}")
    print("Abilities:")
    for ability in abilities:
        print(f"- {ability}")
    print()

average_weight = calculate_average_weight(pokemon_data)
print(f"Average Weight: {average_weight}")
