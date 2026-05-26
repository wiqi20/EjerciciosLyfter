#data: tendrá toda la lógica de exportación e importación de datos.
import csv

def save_students_csv(path,students_list):
    if not students_list:
        print("There are no available data to export")
        return
    with open (path, "w", newline="", encoding="utf-8") as file:
        writer= csv.writer(file)
        writer.writerow(["Name","Section","Spanish","English","Social Studies","Science"])
        for student in students_list:
            writer.writerow([ student["Name"],
                student["Section"],
                student["Spanish"],
                student["English"],
                student["Social Studies"],
                student["Science"]])
    print(f"\nSaved {len(students_list)} students on {path}")


def load_students_csv(path,students_list):
    with open(path,"r",encoding="utf-8") as file:
        reader=csv.DictReader(file,delimiter=",")
        students_list.clear()
        for student in reader:
            student_dict ={
                "Name": student["Name"],
                "Section": student["Section"],
                "Spanish": int(student["Spanish"]),
                "English": int(student["English"]),
                "Social Studies": int(student["Social Studies"]),
                "Science": int(student["Science"])
            }
            students_list.append(student_dict)
    print(f"\nLoaded {len(students_list)} students from {path}")
    # show added data
    print(f"{'Name':30} {'Section':7} {'Spanish':7} {'English':8} {'Social Studies':15} {'Science':7}")
    print("-"*80)
    for student in students_list:
        print(f"{student['Name']:30} {student['Section']:7} {student['Spanish']:7} {student['English']:8} {student['Social Studies']:15} {student['Science']:7}")