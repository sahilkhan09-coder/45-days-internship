import csv


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name} - Price: {self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    
    def add_product(self, product):
        self.products.append(product)

    
    def total_value(self):
        return sum(product.price * product.quantity for product in self.products)


    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None


    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "price", "quantity"])

            for product in self.products:
                writer.writerow(
                    [product.name, product.price, product.quantity]
                )

    
    def load_from_csv(self, filename):
        self.products = []

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                product = Product(
                    row["name"],
                    row["price"],
                    row["quantity"]
                )
                self.products.append(product)



inventory = Inventory()

inventory.add_product(Product("Laptop", 50000, 2))
inventory.add_product(Product("Mouse", 500, 10))
inventory.add_product(Product("Keyboard", 1000, 5))

print("Total Value:", inventory.total_value())

found = inventory.find_product("mouse")
if found:
    print("Found:", found)

inventory.save_to_csv("products.csv")

new_inventory = Inventory()
new_inventory.load_from_csv("products.csv")

print("\nProducts loaded from CSV:")
for product in new_inventory.products:
    print(product)



# staticmethod is a method that does not use self or cls.
#
# load_from_csv could be a static method if it simply reads a file
# and returns data.
#
# It could be a class method if it creates and returns an Inventory object:
#
# classmethod
# def load_from_csv(cls, filename):
#     inventory = cls()
#     ...
#     return inventory
#
# Difference:
# staticmethod -> no access to class or object.
# classmethod -> gets cls and can create class instances.
