'''
Date: 1/2/2025
Name: Frank Huang
Header: String Generation for String Hashing Extended Essay
'''
import os
from random import choice, randint
from string import ascii_letters, digits, punctuation

# Generation Function taken from https://pynative.com/python-generate-random-string/
def generate(length):
   letters = ascii_letters + digits + punctuation
   result_str = ''.join(choice(letters) for i in range(length))
   return result_str
    
# Creating Sample Cases
for i in range(1, 21):
    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath(f"generator/samples/sample_{i*50}_strings", )
    with open(new_path, 'w') as file:
      for j in range(i*50):
         file.write(generate(randint(3, 40)) + "\n")
