from datetime import date

class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth


    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years


def validate_adult(func):
    def wrapper(user: User, *args, **kwargs):
        if user.age < 18:
            raise ValueError(f"The User {user.name} is {user.age}, is not an adult")
        return func(user, *args, **kwargs)
    return wrapper

@validate_adult
def access_service(user: User):
    print(f"Access granted to: {user.name}, age: {user.age}")
    return "Access granted"

try:
    access_service(User("Ana",date(2000, 6, 1)))
    access_service(User("Sara",date(2010, 6, 1)))
except ValueError as e:
    print("Error:", e)