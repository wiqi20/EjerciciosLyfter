import csv
def read_csv(path):
    with open(path,"r",encoding="utf-8") as file:
        reader=csv.DictReader(file,delimiter=",")
        for row in reader:
            print(f"Name: {row['name']}")
            print(f"Genre: {row['genre']}")
            print(f"Developer: {row['developer']}")
            print(f"ESRB Rating: {row['classification']}")
            print("-"*40)


def classification_filter(path):
    filter = input("Enter the ESRB rating you want to search for (example: T, M, E): ").strip()
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        found = False
        for row in reader:
            if row['classification'].strip().upper() == filter.upper():
                print(f"Name: {row['name']}")
                print(f"Genre: {row['genre']}")
                print(f"Developer: {row['developer']}")
                print(f"ESRB Rating: {row['classification']}")
                print("-" * 40)
                found = True
        if not found:
            print(f"No videogames found with classification '{filter}'.")


#read_csv("videogames.csv")
classification_filter("videogames.csv")