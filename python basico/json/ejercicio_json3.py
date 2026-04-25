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


#Print pokemons
def pokemon_data_print(pokemons):
    for pokemon in pokemons:
        print ("Name: ", pokemon["name"]["english"])
        print ("Type: ", ", ".join(pokemon["type"]))
        print ("Level: ", pokemon["level"])
        print ("Base stats: ")
        for stat, value in pokemon["base"].items(): 
            print(f"{stat}: {value}")
        print("-"*30)


def main():
    pokemons=read_json(FILE_PATH)
    pokemon_data_print(pokemons)


main()