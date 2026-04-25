import json
FILE_PATH = "pokemons.json"
# Load JSON and show its content
def read_json(FILE_PATH):
    try:   
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []


def type_pokemon_filter(pokemons):
    pokemon_type = input("Enter the type of the Pokemon to search: ").lower()
    filtered = [p for p in pokemons if pokemon_type in [t.lower() for t in p["type"]]]
    if filtered:
        print("Found pokemons with type: ", pokemon_type)
        for pokemon in filtered:
            print(pokemon["name"]["english"])
        return filtered
    else:
        print("No Pokemon found with type:", pokemon_type)
        return []


def main():
    pokemons=read_json(FILE_PATH)
    type_pokemon_filter(pokemons)


main()