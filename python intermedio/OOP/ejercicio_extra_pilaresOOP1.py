class Employee:
    def __init__(self, name, salary):
        self.__name= name       #private atribute 
        self.__salary= salary   #private atribute 
    
    
    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self,new_name):
        self.__name=new_name


    @property
    def get_salary(self):
        return self.__salary

    @get_salary.setter
    def get_salary(self,new_salary):
        if new_salary>=0:
            self.__salary=new_salary
        else:
            raise ValueError("Salary must be a possitive value")
    
    
    def promote(self,percentage):
        if percentage>0:
            self.__salary*=(1+percentage/100)
            return self.__salary
        else:
            raise ValueError("Promotion percentage must be possitive")
try:
    emp= Employee("Abner",3000)
    print(f"Employee name: {emp.get_name}")
    print(f"Employee salary: {emp.get_salary}")
    emp.promote(10)
    print(f"Employee salary after promotion: {round(emp.get_salary,2)}")
except ValueError as e:
    print("Error:",e)