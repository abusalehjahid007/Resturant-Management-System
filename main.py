from fooditem import FoodItem
from users import Customer, Admin, Employee
from menu import Menu
from resturent import Resturant
from orders import Order
   
res = Resturant("Dhaka Hotel")
   
def Customer_menu():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    customer = Customer(name=name, phone=phone, email=email, address=address)
    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if(choice == "1"):
            customer.view_menu(res)
        elif(choice == "2"):
            item_name = input("Enter Iteam Name: ")
            quant = int(input("Quantity you Need: "))
            customer.add_to_cart(res, item_name, quant)
        elif(choice == "3"):
            customer.view_item()
        elif(choice == "4"):
            customer.pay_bill()
        elif(choice == "5"):
            break
        else:
            print("Invalid choice")
   
    
def Admin_menu():
    name = input("Enter Name: ")
    phoone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    admin = Admin(name, phoone, email, address)
    while True:
        print(f"Welcome {admin.name}")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if(choice == "1"):
            name = input("Enter Item Name: ")
            price = int(input("Enter Item Price: "))
            quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(name, price, quantity)
            admin.add_new_item(res, item)
        elif(choice == "2"):
            name = input("Enter EMP Name: ")
            phoone = input("Enter EMP Phone: ")
            email = input("Enter EMP Email: ")
            address = input("Enter EMP Address: ")
            age = input("Enter EMP Age: ")
            desig = input("Enter EMP Designation: ")
            salary = input("Enter EMP Salary: ")
            emp = Employee(name, phoone, email, address, age, desig, salary)
            admin.add_employee(res, emp)
        elif(choice == "3"):
            admin.view_employee(res)
        elif(choice == "4"):
            admin.sow_item(res)
        elif(choice == "5"):
            name = input("Enter Item Name: ")
            admin.delete_item(res, name)
        elif(choice == "6"):
            break
        else:
            print("Invalid choice")
   
   
   
   
   
while True:
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        Customer_menu()
    elif choice == '2':
        Admin_menu()
    elif choice == '3':
        break
    else:
        print("Invalid choice!!")
        
