#!/usr/bin/python3

# Complete this source code (str = "Holberton School") in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

# You can find the source code here
# The output of the program should be:
# 3 times the value of str
# followed by a new line
# followed by the 9 first characters of str
# followed by a new line
# You are not allowed to use any loops or conditional statement
# Your program should be maximum 5 lines long

string: str = "Holberton School"
first_9_char: str = string[:9]
print(string * 3)
print(first_9_char)
