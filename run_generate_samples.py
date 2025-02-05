from Generator import *
from chaining import *
import time
import csv

gen = Generator(100000, 20, 20, 500)
gen.create_samples() # Adds existing test case file paths to the list of filepaths
print("Generated")