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


read_csv("videogames.csv")