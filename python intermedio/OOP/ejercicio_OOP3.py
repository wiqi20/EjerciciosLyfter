class Student():
    def __init__(self,Name,Spanish,English,Social_Studies,Science):
        self.Name = Name
        self.Spanish = Spanish
        self.English = English
        self.Social_Studies = Social_Studies
        self.Science = Science


    def create_student(students_list):
        Name = input("Enter your Name: ")
        Spanish = int(input("Spanish Score: "))
        English = int(input("English Score: "))
        Social_Studies = int(input("Social Studies Score: "))
        Science = int(input("Science Score: "))
        students_list.append(Student(Name,Spanish,English,Social_Studies,Science))
        print(f"{'Name':30} {'Spanish':7} {'English':8} {'Social Studies':15} {'Science':7}")
        print("-"*80)
        for student in students_list:
            print(f"{student.Name:32} {student.Spanish:5} {student.English:5} {student.Social_Studies:11} {student.Science:12}")


students_list=[]
Student.create_student(students_list)