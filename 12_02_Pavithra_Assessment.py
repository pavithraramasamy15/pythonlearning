"""1. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing item, and calculating the total price.
Expected Output:
Current item in Cart:
Papaya - 100
Guava - 200
Orange - 150
Total Quantity: 450

Updated item in Cart after removing Orange:
Papaya - 100
Guava - 200
Total Quantity: 300
"""

class ShoppingCart():
    def __init__(self):
        self.stock = {}

    def add_item(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity
        else:
            self.stock[item] = quantity

    def remove_item(self, item):
        if item in self.stock:
            del self.stock[item]

    def calculate_total_quantity(self):
        total_quantity = sum(self.stock.values())
        return total_quantity


    def display_cart(self):
        print("Current items in Cart:")
        for item, quantity in self.stock.items():  
            print(f"{item} - {quantity}")
        total_quantity = self.calculate_total_quantity()
        print(f"Total Quantity: {total_quantity}\n")




cart = ShoppingCart()


cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)


cart.display_cart()


cart.remove_item("Orange")


cart.display_cart()

'''
2. Design a class Calculator that performs basic arithmetic operations. The class should have the following methods like add, subtract, multiply and divide, square, square root, power, absolute value, factorial, percentage

Expected Output:

calc = Calculator()
print(calc.add(5, 3))            
# Expected output: 8
print(calc.subtract(10, 4))       
# Expected output: 6
print(calc.multiply(2, 6))        
# Expected output: 12
print(calc.divide(15, 4))         
# Expected output: 3.75
print(calc.square(4))             
# Expected output: 16
print(calc.square_root(9))        
# Expected output: 3.0
print(calc.power(2, 3))           
# Expected output: 8
print(calc.absolute_value(-5))    
# Expected output: 5
print(calc.factorial(5))          
# Expected output: 120
print(calc.percentage(30, 50)) 
'''

import math

class Calculator:
    def __init__(self):
        pass
        
        
    def add(self, x, y):
        return f"Addition: {int(x + y)}"


    def subtract(self, x, y):
       return f"subtraction: {int(x - y)}"

    def multiply(self, x, y):
        return f"multiplication: {int(x * y)}"


    def divide(self, x, y):
        
        return f"divide: {float(x / y)}"

    def square(self, x):
        return f"square: {int(x ** 2)}"

    def square_root(self, x):
        return f"Square root:  {int(x ** 0.5)}"

    def power(self, x, y):
        return f"power: {int(x ** y)}"

    def absolute_value(self, x):
        return f"absolute value:{int(abs(x))}"

    def factorial(self, x):
        return f"factorial:{math.factorial(x)}"
       
    def percentage(self, x, y):
        return f"percentage: {float(x * y) / 100}"


calc = Calculator()
print(calc.add(5, 3))         
print(calc.subtract(10, 4))     
print(calc.multiply(2, 6))        
print(calc.divide(15, 4))       
print(calc.square(4))             
print(calc.square_root(5))        
print(calc.power(2, 3))          
print(calc.absolute_value(-5))   
print(calc.factorial(5))          
print(calc.percentage(30, 50))    

