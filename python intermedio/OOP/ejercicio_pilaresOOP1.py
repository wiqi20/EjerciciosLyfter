# Cree una clase de BankAccount que:
# Tenga un atributo de balance.
# Tenga un método para ingresar dinero.
# Tengo un método para retirar dinero.
# Cree otra clase que herede de esta llamada SavingsAccount que:
# Tenga un atributo de min_balance que se pueda asignar al crearla.
# Arroje un error si al intentar retirar dinero, 
# el retiro haría que el balance quede debajo del min_balance. 
# Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance

class BankAccount:
    def __init__ (self,balance=0):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError ("insufficient funds")

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=100):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            return self.balance
        else:
            print(f"the withdraw amount lower the balance than the minimum balance allowed: {self.min_balance}")
            return self.balance


sa=SavingsAccount(balance=500, min_balance=200)

print(sa.balance)
sa.withdraw(250)
print(sa.balance)
sa.withdraw(100)