'''
Date: 1/2/2025
Name: Frank Huang
Header: String Generation for String Hashing Extended Essay
'''
import os
import math
from random import choice, randint
from string import ascii_letters, digits, punctuation
import time
from Utils import *

class Generator:
   MIN_STR_LENGTH = 5
   MAX_STR_LENGTH = 50

   def __init__(self, max_strings, data_points, num_of_trials):
      self.max_strings = max_strings
      self.data_points = data_points
      self.increment = math.floor(max_strings / data_points)
      self.num_of_trials = num_of_trials
      self.samples = []
      
   # Generation Function taken from https://pynative.com/python-generate-random-string/
   def generate(self, length):
      letters = ascii_letters + digits + punctuation
      result_str = ''.join(choice(letters) for i in range(length))
      return result_str
      
   # Creating Sample Cases
   def create_samples(self):
      telemetry_start = time.time()
      for i in range(1, self.data_points+1):
         for trial in range(self.num_of_trials):
            cur_path = os.path.dirname(__file__)
            new_path = os.path.relpath(f"samples/sample_{i*self.increment}_strings_{trial}", cur_path)
            open(new_path, 'w').close() # Clears file if pre-existing
            with open(new_path, 'w') as file:
               for j in range(i*self.increment):
                  file.write(self.generate(randint(self.MIN_STR_LENGTH, self.MAX_STR_LENGTH)) + "\n")
               file.close()
            self.samples.append(new_path)

         telemetry_time = time.time()
         print("Generated", i, "data points of", self.data_points, "|", Utils.convert(telemetry_time - telemetry_start), "elapsed")

   def add_sample_list(self):
      for i in range(1, self.data_points+1):
         for trial in range(self.num_of_trials):
            cur_path = os.path.dirname(__file__)
            new_path = os.path.relpath(f"samples/sample_{i*self.increment}_strings_{trial}", cur_path)
            self.samples.append(new_path)
