#!/usr/bin/python3

# Write a function that prints the last digit of a number.

# Prototype: def print_last_digit(number):
# Returns the value of the last digit
# You are not allowed to import any module
# You don’t need to understand __import__

def print_last_digit(number: int) -> int:
   last_digit: int = abs(number) % 10
   print(last_digit, end='')
   
   return last_digit
