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


def sort_per_developer(path):
    filter_developer = input("Enter the developer you want to search for: ").strip()
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        found = False
        for row in reader:
            if row['developer'].strip().upper() == filter_developer.upper():
                print(f"Name: {row['name']}")
                print(f"Genre: {row['genre']}")
                print(f"Developer: {row['developer']}")
                print(f"ESRB Rating: {row['classification']}")
                print("-" * 40)
                found = True
        if not found:
            print(f"No videogames found with the developer entered '{filter_developer}'.")


#read_csv("videogames.csv")
sort_per_developer("videogames.csv")