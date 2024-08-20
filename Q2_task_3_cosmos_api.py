import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    formatted_planets = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet['mass'] else 'N/A'
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else 'N/A'
            formatted_planets.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })
    return formatted_planets

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda x: x['mass'] if x['mass'] != 'N/A' else 0)
    return heaviest_planet['name'], heaviest_planet['mass']

planets = fetch_planet_data()

# Print formatted planet data
for planet in planets:
    print(f"Planet: {planet['name']}, Mass: {planet['mass']} kg, Orbit Period: {planet['orbit_period']} days")

# Find and print the heaviest planet
name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")