def count_words(path):	
	try:
		with open(path,"r", encoding="utf-8") as file:
			content=file.read()
			words = content.split()
		return len(words)
	except FileNotFoundError:
		print("Error: el archivo no existe. verifica la ruta y el nombre.")
	except UnicodeDecodeError:
		print("Error: el archivo no es un .txt válido o tiene otra codificación.")


total=count_words("hola mundo.txt")
print(f"El archivo tiene {total} words.")