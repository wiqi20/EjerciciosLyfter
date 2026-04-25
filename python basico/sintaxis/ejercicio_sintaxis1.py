my_num1= int (input("ingrese un número entero "))
my_num_float= float(input("ingrese un número con decimales: "))
my_string1= input("escriba algo: ")
my_string2= input("escriba algo mas: ")
my_list1=[1,2,5,7]
my_list2=[3,4,8,9]
my_bool1=False
my_bool2=True
#sum=my_string1+my_string2 #string+string
#sum=my_string1+my_num1 #string+int TypeError: can only concatenate str (not "int") to str no permite concatenar strings con int
#sum=my_num1+my_string1 #int+string TypeError: can only concatenate str (not "int") to str no permite concatenar strings con int
#sum=my_list1+my_list2 #string+string
#sum=my_string1+my_list1 #TypeError: can only concatenate str (not "list") to str no permite concatenar strings con list
#sum=my_num_float+my_num1 #float+int
sum=my_bool1+my_bool2
print(len(my_string1))
print(sum)
#print(my_list1)
#print(f"{my_string1}/{my_string2}/{my_num1}/{my_num_float}/{my_list1}/{my_bool1}/{my_bool2}")