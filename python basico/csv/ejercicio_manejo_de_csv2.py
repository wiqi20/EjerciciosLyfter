import csv

def save_videogames(path, n):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["name", "genre", "developer", "classification"])
        for i in range(n):
            print(f"\nVideogame {i+1}:")
            name = input("Name: ")
            genre = input("Genre: ")
            developer = input("Developer: ")
            classification = input("ESRB Rating: ")
            writer.writerow([name, genre, developer, classification])
    
    print(f"\nSuccessfully filed {n} video games on '{path}'.")


count = int(input("How many video games do you want to enter? "))
save_videogames("videogames.csv", count)