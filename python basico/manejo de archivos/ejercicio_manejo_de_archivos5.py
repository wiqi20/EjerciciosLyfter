def add_line(path):
    try:
        new_line = input("Escribe una línea de texto: ")
        with open(path, "a", encoding="utf-8") as file:
            file.write(new_line + "\n")

        print(f"La línea se agregó correctamente al archivo '{path}'.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


add_line("hola_mundo.txt")