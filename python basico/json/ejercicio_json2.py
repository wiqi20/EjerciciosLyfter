import json
FILE_PATH = "pokemons.json"
# Load JSON and show its content
def read_json(path):
    try:   
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []

# Write JSON file with new data
def add_pokemon(path, pokemons, pokemon):
    pokemons.append(pokemon)
    with open(path, "w") as file:
        json.dump(pokemons, file, indent=4)


#requesting new Pokemon data from user input
def request_pokemon_data():
    name = input("Enter the name of the Pokemon: ")
    level = int(input("Enter the level of the Pokemon: "))
    type_ = input("Enter the type of the Pokemon (comma separated if multiple): ").split(",")
    base_stats = {}
    base_stats["HP"] = int(input("Enter HP: "))
    base_stats["Attack"] = int(input("Enter Attack: "))
    base_stats["Defense"] = int(input("Enter Defense: "))
    base_stats["Sp. Attack"] = int(input("Enter Sp. Attack: "))
    base_stats["Sp. Defense"] = int(input("Enter Sp. Defense: "))
    base_stats["Speed"] = int(input("Enter Speed: "))

    return {
        "name": {"english": name},
        "level": level,
        "type": [t.strip() for t in type_],
        "base": base_stats
    }


def main():
    pokemons=read_json(FILE_PATH)
    print(f"Found {len(pokemons)} Pokemon existents.")
    new_pokemon = request_pokemon_data()
    add_pokemon(FILE_PATH, pokemons, new_pokemon)
    print(f"Pokemon {new_pokemon['name']['english']} successfully added.")


main()