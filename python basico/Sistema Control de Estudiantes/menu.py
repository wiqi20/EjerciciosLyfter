#menu: tendrá toda la lógica relacionada al menú de opciones.
from actions import request_student_info, check_students_list, students_list

def main_menu():
    while True:
        print("1. Enter new Student")
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
                print("1. Enter new Student")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==1:
                            print("Enter new Student")
                            request_student_info(students_list)
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==2:
                print("2. Check Students List")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==2:
                            print("Check Students List")
                            check_students_list(students_list)
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==3:
                print("3. Show Top 3 for Students Average Score")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==3:
                            print("Show Top 3 for Students Average Score")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==4:
                print("4. Show All Students Average Score")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==4:
                            print("Show All Students Average Score")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==5:
                print("5. Export Data to CSV")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==5:
                            print("Export Data to CSV")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==6:
                print("6. Import Data From CSV")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==6:
                            print("Import Data From CSV")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==7:
                print("7. Delete Student")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==7:
                            print("Delete Student")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==8:
                print("8. Show Failed Students")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==8:
                            print("Show Failed Students")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==9:
                print("Closing the system...")
                break
            else:
                print("Select a valid option")
        except ValueError:
            print("Enter an integer number")
def main_menu():
    while True:
        print("1. Enter new Student")
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
                print("1. Enter new Student")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==1:
                            print("Enter new Student")
                            request_student_info(students_list)
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==2:
                print("2. Check Students List")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==2:
                            print("Check Students List")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==3:
                print("3. Show Top 3 for Students Average Score")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==3:
                            print("Show Top 3 for Students Average Score")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==4:
                print("4. Show All Students Average Score")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==4:
                            print("Show All Students Average Score")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==5:
                print("5. Export Data to CSV")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==5:
                            print("Export Data to CSV")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==6:
                print("6. Import Data From CSV")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==6:
                            print("Import Data From CSV")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==7:
                print("7. Delete Student")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==7:
                            print("Delete Student")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==8:
                print("8. Show Failed Students")
                print("0. Return to main menu")
                while True:
                    try:    
                        option_secundary_menu=int(input("\nSelect an option: "))
                        if option_secundary_menu==8:
                            print("Show Failed Students")
                        elif option_secundary_menu==0:
                            break
                        else:
                            print("Select a valid option")
                    except ValueError:
                        print("Enter an integer number")
            elif option_main_menu==9:
                print("Closing the system...")
                break
            else:
                print("Select a valid option")
        except ValueError:
            print("Enter an integer number")
#main_menu()