def read_file_per_line(path):	
	try:
		with open(path,"r", encoding="utf-8") as file:
			lines=file.readlines()
		return lines
	except FileNotFoundError:
		print("Error: el archivo no existe. verifica la ruta y el nombre.")
	except UnicodeDecodeError:
		print("Error: el archivo no es un .txt válido o tiene otra codificación.")


def remove_line_break(lines):
	no_line_break=" ".join(line.strip() for line in lines)
	return no_line_break


def create_new_file(no_line_break):
	with open("new_file.txt","w", encoding="utf-8") as new_file:
		new_file.write(no_line_break)
	with open ("new_file.txt","r", encoding="utf-8") as new_file:
		content=new_file.read()
		print(content)


lines=read_file_per_line('hola mundo.txt')
no_line_break=remove_line_break(lines)
create_new_file(no_line_break)