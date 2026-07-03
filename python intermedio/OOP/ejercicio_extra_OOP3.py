class Product:
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity


    def __str__(self):
        return f"{self.name} - Price: {self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.inventory=[]


    def add_product(self, product):
        self.inventory.append(product)


    def show_all_products(self):
        for product in self.inventory:
            print(product)


    def calculate_inventory_value(self):
        total=0
        for product in self.inventory:
            total += product.price*product.quantity
        
        return print(f"The total inventory value is: {total}")


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

inventory=Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

inventory.show_all_products()
inventory.calculate_inventory_value()
