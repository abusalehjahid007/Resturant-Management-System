
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
        
    def view_menu(self, resturant):
        resturant.menu.show_menu()
        
    def add_to_cart(self, resturant, item_name, quantity):
        item = resturant.menu.find_iteam(item_name)
        if item:
            if item.quantity >= quantity:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added to cart")
            else:
                print("Sorry, we don't have enough quantity of this item.")
        else:
            print("Item not found in the menu")
    
    def view_item(self):
        print("*****View Cart*****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price()}")
        
        
class Order:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity
    
    def remove(self, item):
        if item in self.items:
            del self.items[item]
            
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
       
    def clear(self):
        self.items.clear()
       
       
class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
        
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self, resturant, employee):
        resturant.add_employee(employee)
        
    def view_employee(self, resturant):
        resturant.view_employee()
        
    def add_new_item(self, resturant, item):
        resturant.menu.add_menu_item(item)
        
    def delete_item(self, resturant, item):
        resturant.menu.remove_item(item)
         
class Resturant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()
        
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is added!")
        
    def view_employee(self):
        print("Employee List..!")
        for emp in self.employees:
            print(f"Name: {emp.name}, Email: {emp.email}, Phone: {emp.phone}, Address: {emp.address}")
        
        
        
class Menu:
    def __init__(self):
        self.items = []
        
    def add_menu_item(self, item):
        self.items.append(item)
    
    def find_iteam(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_iteam(item_name)
        
        if item:
            self.items.remove(item)
        else:
            print("Item not found!")
            
    def show_menu(self):
        print("*******Menu*******")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
            
class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        

# item1 = FoodItem("Burger", 10.99, 100)
# item2 = FoodItem("Pizza", 12.99, 50)

# mamr_res = Resturant("Dhaka hotel")
# admin = Admin("rakib", 1421424, "rakib@gmail", "Dhaka")
# admin.add_new_item(mamr_res, item1)
# admin.add_new_item(mamr_res, item2)
# customer1 = Customer("rakib", 1421424, "rakib@gmail", "Dhaka")
# customer1.view_menu(mamr_res)

# customer1.add_to_cart(mamr_res, "burger", 101)
# customer1.view_item()