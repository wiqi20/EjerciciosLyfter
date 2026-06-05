#actions: tendrá toda la lógica de las acciones del menú, excepto las de exportar e importar datos.
import re
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
    pattern = r"^\d{1,2}[A-Z]$"
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

class Student:
    def __init__(self,name, section, spanish, english, social_studies, science):
        self.name = name
        self.section = section
        self.spanish = int (spanish)
        self.english = int (english)
        self.social_studies = int (social_studies)
        self.science = int (science)


    def request_student_info (students_list):
        while True:
            name=validate_name()
            section=validate_section()
            if student_exists(name, section, students_list):
                print("Error: The entered Student and Section already exists")
            else:
                break
        spanish = validate_grade("Spanish")
        english = validate_grade("English")
        social_studies = validate_grade("Social Studies")
        science = validate_grade("Science")
        
        student = Student(name, section, spanish, english, social_studies, science)
        students_list.append(student)

        print("\nStudent added correctly:")
        return(check_students_list(students_list))


def check_students_list(students_list):
    if not students_list:
        print("There are no students in data base")
        return
    
    print(f"{'Name':30} {'Section':7} {'Spanish':7} {'English':8} {'Social Studies':15} {'Science':7}")
    print("-"*80)
    for student in students_list:
        print(f"{student.name:32} {student.section:8} {student.spanish:5} {student.english:5} {student.social_studies:11} {student.science:12}")


#this is the 3 option in menu Show Top 3 for Students Average Score
def top_students_average_score(students_list):
    if not students_list:
        print("There are no students in data base")
        return
    students_average_score_list=[]
    for student in students_list:
        average_score= (student["Spanish"]+student["English"]+student["Social Studies"]+student["Science"])/4
        students_average_score_list.append({
            "Name": student["Name"],
            "Section": student["Section"],
            "Average Score": round(average_score,2)
        })
    sorted_students_score=sorted(students_average_score_list, key=lambda x: x["Average Score"], reverse=True)
    print(f"{'Name':20} {'Section':10} {'Average Score'}")
    print("-"*46)
    for student in sorted_students_score[:3]:
        print(f"{student['Name']:20} {student['Section']:10} {student['Average Score']}")


#this funtion calculate the average score per student
def show_individual_average_score(students_list):
    students_average_score_list=[]
    for student in students_list:
        average_score= (student["Spanish"]+student["English"]+student["Social Studies"]+student["Science"])/4
        students_average_score_list.append({
            "Name": student["Name"],
            "Section": student["Section"],
            "Average Score": round(average_score,2)
        })
    print(f"{'Name':20} {'Section':10} {'Average Score'}")
    print("-"*46)
    for student in students_average_score_list:
        print(f"{student['Name']:20} {student['Section']:10} {student['Average Score']}")


#this is the 4 option in menu Show All Students Average Score
def show_all_students_average_score(students_list):
    if not students_list:
        print("There are no students in data base")
        return
    students_scores_list=[]
    for student in students_list:
        for subject in ["Spanish", "English", "Social Studies","Science"]:
            students_scores_list.append(student[subject])
    all_students_average_score=sum(students_scores_list)/len(students_scores_list)
    print("The average score for students in data base is: ",round(all_students_average_score,2))


def delete_student(students_list):
    if not students_list:
        print("There are no students in data base")
        return
    name=validate_name()
    section=validate_section()
    if student_exists(name, section, students_list):
        delete=input(f"The Student {name} from section {section} exist, do you want to delete it (Y/N): ")
        if delete.lower()=="y":
            students_list[:]=[stdnt for stdnt in students_list if not (stdnt["Name"].lower()==name.lower() and stdnt["Section"].upper()== section.upper())]
            print(f"The Student {name} from section {section} was deleted correctly")
        else:
            return
    else:
        print(f"The Student {name} from section {section} doesn't exist")


def show_failed_students(students_list):
    if not students_list:
        print("There are no students in data base")
        return
    failed_students_list=[]
    for student in students_list:
        if student["Spanish"] <60:
            failed_students_list.append({
            "Name": student["Name"],
            "Section": student["Section"],
            "Subject": "Spanish",
            "Score": student["Spanish"]
        })
        if student["English"]<60:
            failed_students_list.append({
            "Name": student["Name"],
            "Section": student["Section"],
            "Subject": "English",
            "Score": student["English"]
        })        
        if student["Social Studies"]<60:
            failed_students_list.append({
            "Name": student["Name"],
            "Section": student["Section"],
            "Subject": "Social Studies",
            "Score": student["Social Studies"]
        })
        if student["Science"]<60:
            failed_students_list.append({
            "Name": student["Name"],
            "Section": student["Section"],
            "Subject": "Science",
            "Score": student["Science"]
        })
        if not failed_students_list:
            print("There are no failed students this time.")
        else:
            print(f"{'Name':20} {'Section':10} {'Subject':15}{'Score'}")
            print("-"*55)
            for student in failed_students_list:
                print(f"{student['Name']:20} {student['Section']:10} {student['Subject']:15} {student['Score']}")