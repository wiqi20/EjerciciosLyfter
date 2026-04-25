#Agrupar empleados por departamento
#Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
dict_by_dpt={}
for employee in employees:
    dept=employee["department"]
    if dept not in dict_by_dpt:
        dict_by_dpt[dept]=[employee]
    else:
        dict_by_dpt[dept].append(employee)
for dept, employees in dict_by_dpt.items():
    print(f"Departamento: {dept}")
    for employee in employees:
        print(f"Nombre: {employee['name']}, Correo: {employee['email']}")