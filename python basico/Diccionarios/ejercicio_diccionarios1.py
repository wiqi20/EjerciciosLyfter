#Cree un diccionario que guarde la siguiente información sobre un hotel:
#nombre,numero_de_estrellas,habitaciones
#El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
#numero, piso, precio_por_noche 
my_dictionary={
    "name":"Mi hotel",
    "stars":5,
    "rooms":[
    {
        "Number":1,
        "Floor":1,
        "Price":1200,
    },
    {
        "Number":10,
        "Floor":2,
        "Price":3000,
    },
    {
        "Number":20,
        "Floor":3,
        "Price":5000,
    },
    ],
}
print(my_dictionary)
print ("Hello everyone")