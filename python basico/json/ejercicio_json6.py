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


#Calculate average level per type
def average_level_type(pokemons):
    level_per_type={}
    for pokemon in pokemons:
        for pokemon_type in pokemon["type"]:
            if pokemon_type not in level_per_type:
                level_per_type[pokemon_type]=[]
            level_per_type[pokemon_type].append(pokemon["level"])
    level_average= {pokemon_type:sum(levels)/len(levels) for pokemon_type, levels in level_per_type.items()}
    for pokemon_type, average in level_average.items():
        print(f"Type: {pokemon_type} -> average level: {average:.2f}")
    return level_average


def main():
    pokemons=read_json(FILE_PATH)
    average_level_type(pokemons)

main()