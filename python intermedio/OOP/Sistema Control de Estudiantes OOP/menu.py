#menu: tendrá toda la lógica relacionada al menú de opciones.
import csv
from actions import request_student_info, check_students_list, top_students_average_score, show_all_students_average_score, delete_student, show_failed_students
from data import save_students_csv,load_students_csv
def main_menu():
    students_list = []
    while True:
        print("\n1. Enter new Student")
        print("2. Check Students List")
        print("3. Show Top 3 for Students Average Score ")
        print("4. Show All Students Average Score")
        print("5. Export Data to CSV")
        print("6. Import Data From CSV")
        print("7. Delete Student")
        print("8. Show Failed Students")
        print("9. Exit")
        try:
            option_main_menu=int(input("\nSelect an option: "))
            if option_main_menu==1:
                print("\nAdding new Student\n")
                request_student_info(students_list)
            elif option_main_menu==2:
                print("\nCheck Students List\n")
                check_students_list(students_list)
            elif option_main_menu==3:
                print("\nShowing Top 3 for Students Average Score\n")
                top_students_average_score(students_list)
            elif option_main_menu==4:
                print("\nShowing All Students Average Score\n")
                show_all_students_average_score(students_list)
            elif option_main_menu==5:
                if students_list:
                    print("\nExport Data to CSV\n")
                    path=input("CSV file path: ")
                    save_students_csv(path,students_list)
                else:
                    print("There are no available data to export")
            elif option_main_menu==6:
                try:
                    print("\nImport Data From CSV\n")
                    path=input("CSV file path: ")
                    load_students_csv(path,students_list)
                except FileNotFoundError:
                    print("Entered path not found")
            elif option_main_menu==7:
                print("\nDelete Student\n")
                delete_student(students_list)
            elif option_main_menu==8:
                print("\nShowing Failed Students\n")
                show_failed_students(students_list)
            elif option_main_menu==9:
                print("Closing the system...")
                break
            else:
                print("Select a valid option")
        except ValueError:
            print("Enter an integer number")