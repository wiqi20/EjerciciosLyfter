#Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.
discount1=0.02
discount2=0.10
price=int(input("Ingrese el precio del producto "))
if price<100:
    final_price=price-(price*discount1)
    print(final_price)
elif price>=100:
    final_price=price-(price*discount2)
    print(final_price)