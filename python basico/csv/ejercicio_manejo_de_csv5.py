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


def count_per_genre(path):
    count={}
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            genre=row['genre'].strip()
            count[genre]=count.get(genre,0)+1
    organized=sorted(count.items(),key=lambda x: x[1], reverse=True)
    print("\nAmount of Videogames per Genre: ")
    for genre, amount in organized:
        print(f"{genre}: {amount}")


#read_csv("videogames.csv")
count_per_genre("videogames.csv")