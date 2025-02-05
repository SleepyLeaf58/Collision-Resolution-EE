'''
Date: 1/2/2025
Name: Frank Huang
Header: String Generation for String Hashing Extended Essay
'''
import os
import math
from random import choice, randint, shuffle
from string import ascii_letters, digits, punctuation
import time
from Utils import *

class Generator:
   MIN_STR_LENGTH = 5
   MAX_STR_LENGTH = 50

   def __init__(self, max_strings, data_points, num_of_trials, num_cases):
      self.max_strings = max_strings
      self.data_points = data_points
      self.increment = math.floor(max_strings / data_points)
      self.num_of_trials = num_of_trials
      self.num_cases = num_cases
      
   ''' Generation Function taken from https://pynative.com/python-generate-random-string/ '''
   def generate(self, length):
      letters = ascii_letters + digits + punctuation
      result_str = ''.join(choice(letters) for i in range(length))
      return result_str
      
   ''' Generate Random String'''
   def gen_string(self):
      return self.generate(randint(self.MIN_STR_LENGTH, self.MAX_STR_LENGTH))
   
   ''' Creating Sample Cases '''
   def create_samples(self):
      telemetry_start = time.time()
      for i in range(1, self.data_points+1):
         for trial in range(self.num_of_trials):
            cur_path = os.path.dirname(__file__)
            new_path = os.path.relpath(f"samples/sample_{i*self.increment}_strings_{trial}", cur_path)
            open(new_path, 'w').close() # Clears file if pre-existing
            with open(new_path, 'w') as file:
               for j in range(i*self.increment):
                  file.write(self.gen_string() + '\n')
               file.close()

         telemetry_time = time.time()
         print("Generated", i, "data points of", self.data_points, "|", Utils.convert(telemetry_time - telemetry_start), "elapsed")

   # def add_sample_list(self):
   #    telemetry_start = time.time()

   #    for i in range(1, self.data_points+1):
   #       for trial in range(self.num_of_trials):
   #          cur_path = os.path.dirname(__file__)
   #          new_path = os.path.relpath(f"samples/sample_{i*self.increment}_strings_{trial}", cur_path)
   #          self.samples.append(new_path)

   def add_search_cases(self):
         # Randomizing number of successful/unsuccessful searches
         successful_searches = randint(0, self.num_cases)
         unsuccessful_searches = self.num_cases - successful_searches
         
         telemetry_start = time.time()

         for i in range(1, self.data_points+1):
            for trial in range(self.num_of_trials):
               cur_path = os.path.dirname(__file__)
               new_path = os.path.relpath(f"samples/sample_{i*self.increment}_strings_{trial}", cur_path)

               # Setting Search Cases
               shuffle_list = [i for i in range(i*self.increment)]
               #print(shuffle_list)
               shuffle(shuffle_list)

               search_cases = []

               case_indexes = [shuffle_list[i] for i in range(successful_searches)]
               #print(i*self.increment, new_path)
               with open(new_path, 'r') as file:
                  for j in range(i*self.increment):
                     current_str = file.readline()
                     if j in case_indexes:
                        search_cases.append(current_str)
                        #print("String", current_str)
               #print(search_cases)

               write_path = os.path.relpath(f"search_cases/case_{i*self.increment}_strings_{trial}", cur_path)
               open(write_path, 'w').close() # Clears file if pre-existing
               with open(write_path, 'w') as file:
                  for case in search_cases:
                     file.write(case)

                  for j in range(unsuccessful_searches):
                     file.write(self.gen_string()+'\n')
                  file.close()

               telemetry_time = time.time()

            print(i, "cases created of", self.data_points, "|", Utils.convert(telemetry_time-telemetry_start), "elapsed")                 

