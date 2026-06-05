#data: tendrá toda la lógica de exportación e importación de datos.
import csv
from actions import Student


def save_students_csv(path,students_list):
    if not students_list:
        print("There are no available data to export")
        return
    with open (path, "w", newline="", encoding="utf-8") as file:
        writer= csv.writer(file)
        writer.writerow(["Name","Section","Spanish","English","Social Studies","Science"])
        for student in students_list:
            writer.writerow([ student.name,
                student.section,
                student.spanish,
                student.english,
                student.social_studies,
                student.science])
    print(f"\nSaved {len(students_list)} students on {path}")


def load_students_csv(path,students_list):
    with open(path,"r",encoding="utf-8") as file:
        reader=csv.DictReader(file,delimiter=",")
        students_list.clear()
        for row in reader:
            student = Student (
                row["Name"],
                row["Section"],
                row["Spanish"],
                row["English"],
                row["Social Studies"],
                row["Science"])
            students_list.append(student)
    print(f"\nLoaded {len(students_list)} students from {path}")
    # show added data
    print(f"{'Name':30} {'Section':7} {'Spanish':7} {'English':8} {'Social Studies':15} {'Science':7}")
    print("-"*80)
    for student in students_list:
        print(f"{student.name:30} {student.section:7} {student.spanish:7} {student.english:8} {student.social_studies:15} {student.science:7}")