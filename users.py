
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
        
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
        self.employees = []
    
    def add_employee(self, name, email, phone, address, age, designation, salary):
        employee = Employee(name, email, phone, address, age, designation, salary)
        self.employees.append(employee)
        print(f"{employee.name} is added!")
        
    def view_employee(self):
        print("Employee List..!")
        for emp in self.employees:
            print(f"Name: {emp.name}, Email: {emp.email}, Phone: {emp.phone}, Address: {emp.address}")
         
         