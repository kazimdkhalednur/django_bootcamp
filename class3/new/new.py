# from .. import main

# obj = main.An()
# print(obj)

# class ASd:
#     def display(self):
#         print("this is ASd")

from os.path import abspath, dirname
import sys

# Get the directory of current file
current_dir = dirname(abspath(__file__))
print(current_dir)

# Get the directory of main.py
parent_dir = dirname(current_dir)
print(parent_dir)


# # Add the parent directory to the system path
sys.path.append(parent_dir)

from main import Animal

obj = Animal("Tiger")
print(obj)