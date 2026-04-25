def read_file_per_line(path):	
	try:
		with open(path,"r", encoding="utf-8") as file:
			lines=file.readlines()
		return lines
	except FileNotFoundError:
		print("Error: el archivo no existe. verifica la ruta y el nombre.")
	except UnicodeDecodeError:
		print("Error: el archivo no es un .txt válido o tiene otra codificación.")


def convert_uppercase (lines):
	upper_case="".join(line.upper() for line in lines)
	return upper_case


def create_new_file(upper_case):
	with open("new_file.txt","w", encoding="utf-8") as new_file:
		new_file.write(upper_case)
	with open ("new_file.txt","r", encoding="utf-8") as new_file:
		content=new_file.read()
		print(content)


lines=read_file_per_line('hola mundo.txt')
upper_case=convert_uppercase (lines)
create_new_file(upper_case)