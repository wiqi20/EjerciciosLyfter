#main: tendrá el punto de entrada del programa.
from menu import main_menu
from actions import check_students_list,request_student_info,students_list

def main():
    print("Students Control System\n")
    main_menu()


if __name__ == "__main__":
    main()