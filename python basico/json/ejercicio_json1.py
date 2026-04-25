import json
# Cargar el archivo JSON y mostrar su contenido
def read_json(path):
    with open(path, "r") as file:
        pokemons = json.load(file)
    print(pokemons)


# Escribir archivo JSON con nuevos datos
def write_json(path, pokemons):
    with open(path, "w") as file:
        json.dump(pokemons, file, indent=4)

# Ejemplo de uso
read_json("pokemons.json")