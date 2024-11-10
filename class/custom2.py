# Import our custom module using an alias.
import random as r
from import_files import mymodule as s

v = s.add(r.randint(1, 100),r.randint(1, 100))
print(v)
