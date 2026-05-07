#actions: tendrá toda la lógica de las acciones del menú, excepto las de exportar e importar datos.
import re
#students_list=[]
#students_average_score_list=[]
students_list = [
    {'Name': 'Abner Villalobos', 'Section': '11A', 'Spanish': 100, 'English': 58, 'Social Studies': 80, 'Science': 98},
    {'Name': 'Abigail Guzman', 'Section': '11C', 'Spanish': 98, 'English': 99, 'Social Studies': 100, 'Science': 78},
    {'Name': 'Samuel Makai', 'Section': '11B', 'Spanish': 88, 'English': 79, 'Social Studies': 80, 'Science': 99},
    {'Name': 'Sarahi Villalobos', 'Section': '11A', 'Spanish': 100, 'English': 95, 'Social Studies': 100, 'Science': 89}
]
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
    return(check_students_list(students_list))


def check_students_list(students_list):
    print(f"{'Name':30} {'Section':7} {'Spanish':7} {'English':8} {'Social Studies':15} {'Science':7}")
    print("-"*80)
    for student in students_list:
        print(f"{student['Name']:32} {student['Section']:8} {student['Spanish']:5} {student['English']:5} {student['Social Studies']:11} {student['Science']:12}")


#calculate average score per student and create new list to use it later only with average score
def calculate_average_score(students_list):
    students_average_score_list=[]
    for student in students_list:
        average_score= (student["Spanish"]+student["English"]+student["Social Studies"]+student["Science"])/4
        students_average_score_list.append({
            "Name": student["Name"],
            "Section": student["Section"],
            "Average Score": round(average_score,2)
        })
    return students_average_score_list


#this is the 4 option in menu Show All Students Average Score
def show_all_students_average_score(students_average_score_list):
    print(f"{'Name':20} {'Section':10} {'Average Score'}")
    print("-"*46)
    for student in students_average_score_list:
        print(f"{student["Name"]:20} {student["Section"]:10} {student["Average Score"]}")


#this is the 3 option in menu Show Top 3 for Students Average Score
def top_students_average_score(students_average_score_list):
    sorted_students_score=sorted(students_average_score_list, key=lambda x: x["Average Score"], reverse=True)
    print(f"{'Name':20} {'Section':10} {'Average Score'}")
    print("-"*46)
    for student in sorted_students_score[:3]:
        print(f"{student["Name"]:20} {student["Section"]:10} {student["Average Score"]}")


def delete_student(students_list):
    name=validate_name()
    section=validate_section()
    if student_exists(name, section, students_list):
        students_list[:]=[stdnt for stdnt in students_list if not (stdnt["Name"].lower()==name.lower() and stdnt["Section"].upper()== section.upper())]
        print(f"The Student {name} from section {section} was deleted correctly")
    else:
        print(f"The Student {name} from section {section} doesn't exist")

    #     delete_option=int(input("Do you want to delete this Student\n1. Yes\n2. No\n "))
    #             try:
    #                 if delete_option==1:
    #                     print("Deleting the entered Student")
    #                     students_list.p
    #                 elif delete_option ==2:
    #                     break
    #             except:
    #                 print("please select a valid option")
    #         else:
    #             print("The Student you entered doesn't exist!!")
    #             break
    # except:
    #     print("please enter a valid option")

#all_students_average_score(students_list)
#request_student_info(students_list)