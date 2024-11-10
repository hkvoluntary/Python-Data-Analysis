# Importing the user-defined module
from import_files import mymodule

# Using functions from the module
a = 10
b = 5

print(f"{a} + {b} = {mymodule.add(a, b)}")
print(f"{a} - {b} = {mymodule.subtract(a, b)}")
print(f"{a} * {b} = {mymodule.multiply(a, b)}")
print(f"{a} / {b} = {mymodule.divide(a, b)}")

