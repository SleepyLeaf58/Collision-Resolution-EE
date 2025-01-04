from Generator import *
from chaining import *
import time
import csv

gen = Generator(100000, 20, 10)
gen.create_samples() # Adds existing test case file paths to the list of filepaths
gen.add_sample_list()
print("Generated")
print(gen.samples)