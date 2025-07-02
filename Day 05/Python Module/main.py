from addition import add_number,subtract_number
import math
import random

result = add_number(2 , 3)
print(f"Sum is : {result}")

result_2 = subtract_number(5 , 3)
print(f"Defferent is : {result_2}")

print(f"Pie value is {math.pi}") # Import from python standard library module


factorial_Value = 5
print(f"{factorial_Value} Factorial value is {math.factorial(factorial_Value)}")

print(f"Random Number: {random.randint(1, 100)}")
print(f"Random Number: {random.randrange(101)}") 