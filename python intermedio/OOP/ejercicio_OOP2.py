class Person:
    def __init__(self,name):
        self.name=name


class Bus:
    def __init__(self,max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []


    def add_passenger(self,person):
        if len(self.passengers)< self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} just abord the bus")
        else:
            print("There are no available spaces on the bus")


    def delete_passenger(self,person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} just left the bus")
        else:
            print(f"{person.name} Wasn't on the bus")


person_1 = Person("Abner")
person_2 = Person("Abel")
person_3 = Person("Miguel")
person_4 = Person("Petronilo")

bus = Bus(max_passengers=3)
bus.add_passenger(person_1)
bus.add_passenger(person_2)
bus.add_passenger(person_3)
bus.add_passenger(person_4)

bus.delete_passenger(person_2)
bus.delete_passenger(person_4)