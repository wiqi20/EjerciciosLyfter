#Dada n cantidad de notas de un estudiante, calcular:
#Cuantas notas tiene aprobadas (mayor a 70).
#Cuantas notas tiene desaprobadas (menor a 70).
#El promedio de todas.
#El promedio de las aprobadas.
#El promedio de las desaprobadas.
count=int(input("cuantas notas desea ingresar? "))
notes=[]
approved=[]
failed=[]
while count !=0:
    note=int(input("ingrese una nota "))
    notes.append(note)
    if note<70:
        failed.append(note)
    elif note>=70: # el enunciado dejaba fuera el caso que la nota fuese 70
        approved.append(note)
    count -=1
average_total=sum(notes)/len(notes)
average_approved=sum(approved)/len(approved) if len(approved)>0 else 0
average_failed=sum(failed)/len(failed) if len(failed) else 0
print(f"El estudiante tiene {len(approved)} notas aprobadas")
print(f"El estudiante tiene {len(failed)} notas desaprobadas")
print(f"El promedio de todas las notas es {average_total}")
print(f"El promedio de todas las notas aprobadas es {average_approved}")
print(f"El promedio de todas las notas desaprobadas es {average_failed}")