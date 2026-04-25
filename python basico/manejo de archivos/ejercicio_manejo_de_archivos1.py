def read_file_per_line(path):	
	try:
		with open(path,"r", encoding="utf-8") as file:
			lines=file.readlines()
		return lines
	except FileNotFoundError:
		print("Error: el archivo no existe. verifica la ruta y el nombre.")
	except UnicodeDecodeError:
		print("Error: el archivo no es un .txt válido o tiene otra codificación.")

def sort_lines(lines):
	lines.sort() 
	return lines

def create_sorted_file(lines):
	with open("ordenado.txt","w", encoding="utf-8") as file:
		for line in lines:
			file.write(line)
			print(line.strip())#elimina el salto de linea 


lines=read_file_per_line('lista de canciones.txt')
sorted_lines=sort_lines(lines)
create_sorted_file(sorted_lines)