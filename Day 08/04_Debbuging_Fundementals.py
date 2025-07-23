import pdb

def multification(a, b):
    return a * b

pdb.set_trace()
x = input("Enter a number: ")
y = input("Enter another number: ")

result = multification(x, y)
print(f"{x} * {y} = {result}")