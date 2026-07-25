class Employee:
    def __init__(self, name, salary):
        self.__name= name       #private atribute 
        self.__salary= salary   #private atribute 
    
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name=new_name


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,new_salary):
        if new_salary>=0:
            self.__salary=new_salary
        else:
            raise ValueError("Salary must be a possitive value")
    
    
    def promote(self,percentage):
        if percentage>0:
            self.__salary*=(1+percentage)
            return self.__salary
        else:
            raise ValueError("Promotion percentage must be possitive")
try:
    emp= Employee("Abner",3000)
    print(f"Employee name: {emp.name}")
    print(f"Employee salary: {emp.salary}")
    emp.promote(0.1)
    print(f"Employee salary after promotion: {round(emp.salary,2)}")
except ValueError as e:
    print("Error:",e)