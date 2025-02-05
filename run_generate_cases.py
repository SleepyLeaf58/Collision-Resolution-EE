from Generator import *
from chaining import *
import time
import csv

gen = Generator(100000, 20, 20, 500)
gen.add_search_cases()
print("Generated")