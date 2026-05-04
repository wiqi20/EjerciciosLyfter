#actions: tendrá toda la lógica de las acciones del menú, excepto las de exportar e importar datos.
import re
students_list=[]
# contains all related to add new student including the proper validations to each input
def validate_name():
    while True:
        name=input("Name: ").strip()
        if not name:
            print("Error: Name can't be empty")
            continue
        if not re.match(r"^[A-Za-z\s]+$",name):
            print("Error: Name must contain only letters and spaces")
            continue
        return name


def validate_section(): #validate section using regular expresions
    pattern = r"^\d{2}[A-Z]$"
    while True:
        section=input("Section (example: 11A, 12B): ").strip().upper()
        if re.match(pattern,section):
            return section
        else:
            print("Error: Section must be this format (11A, 12B...)")


def student_exists(name,section, students_list):
    return any(stdnt["Name"].lower()== name.lower() and stdnt["Section"].upper()==section.upper() for stdnt in students_list)


def validate_grade(subject):
    while True:
        try:
            grade= int(input(f"{subject} grade (0-100): "))
            if 0 <= grade <=100:
                return grade
            else:
                print("Error: Grade must be between 0 and 100")
        except ValueError:
            print("Error: Enter a valid integer number.")


def request_student_info (students_list):
    students_dict={}
    print("Adding new Student\n")
    while True:
        name=validate_name()
        section=validate_section()
        if student_exists(name, section, students_list):
            print("Error: The entered Student and Section already exists")
        else:
            students_dict["Name"]=name
            students_dict["Section"]=section
            break
    students_dict["Spanish"]=validate_grade("Spanish")
    students_dict["English"]=validate_grade("English")
    students_dict["Social Studies"]=validate_grade("Social Studies")
    students_dict["Science"]=validate_grade("Science")
    students_list.append(students_dict)
    print("\nStudent added correctly:")
    #print(check_students_list(students_list))
    # print("\nesta es la lista\n")
    # print(students_list)
    return(check_students_list(students_list))


def check_students_list(students_list):
    print(f"{'Name':30} {'Section':7} {'Spanish':7} {'English':8} {'Social Studies':15} {'Science':7}")
    print("-"*80)
    for student in students_list:
        print(f"{student['Name']:32} {student['Section']:8} {student['Spanish']:5} {student['English']:5} {student['Social Studies']:11} {student['Science']:12}")
    # for student in students_list:
    #     print(f"Name: {student["Name"]}")
    #     print(f"Section: {student["Section"]}")
    #     print(f"Spanish: {student["Spanish"]}")
    #     print(f"English: {student["English"]}")
    #     print(f"Social Studies: {student["Social Studies"]}")
    #     print(f"Science: {student["Science"]}")
    #     print("-"*30)


request_student_info(students_list)