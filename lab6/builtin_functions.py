import time
from math import sqrt,prod

# 1 Write a Python program with builtin function to multiply all the numbers in a list
def multiply(l):
    return prod(l)  # product of all elements

# 2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def upper_lower_case(s):
    g, k = 0, 0
    for leta in s:
        if leta.islower():
            g+=1
        if leta.isupper():
            k+=1
    return f"Uppercases {g}\nLowercases {k}"

# 3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def palindrome(s):
    return s == s[::-1]

# 4 Write a Python program that invoke square root function after specific milliseconds
def wait_before_invoke(x,t):
    time.sleep(t/1000)    # the function will return after (t/1000) seconds
    return sqrt(x)

# 5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
def tuple_elements(a):
    return all(a)  # returns True if all elements True

