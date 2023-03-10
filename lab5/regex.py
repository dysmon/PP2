import re

#Exercise 1 - Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s. 
def zeroOrMore():
    s = input("Enter a string: ")
    x = re.findall(r"ab*",s)
    print(x)

#Exercise 2 - Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def twoOrThree():
    s = input("Enter a string: ")
    x = re.findall(r"ab{2,3}",s)
    print(x)

#Exercise 3 - Write a Python program to find sequences of lowercase letters joined with a underscore.
def sequenceOfLower(s):
    result = ""
    for i in range(len(s)):
        if i > 0 and s[i-1].islower() and s[i].islower():
            result += "_"
        result += s[i]
    return result

#Exercise 4 - Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def upperLower():
    s = input("Enter a string: ")
    x = re.findall(r"[A-Z][a-z]+",s)
    print(x)

#Exercise 5 - Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def startAendB():
    s = input("Enter a string: ")
    x = re.findall(r"a.*b",s)
    print(x)

#Exercise 6 - Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def replace():
    s = input("Enter a string: ")
    x = re.sub(r"[.]|[ ]|[,]",":",s)
    print(x) 

#Exercise 7 - Write a python program to convert snake case string to camel case string.
def snake_to_camel(s):
    s = s.split("_")
    x = s[0]
    if len(s)>1:
        for i in range(1, len(s)):
            x += s[i].capitalize()
        return x
    return x

#Exercise 8 - Write a Python program to split a string at uppercase letters.
def splitByUpper():
    s = input("Enter a string: ")
    x = re.split("[A-Z]+",s)
    print(x)

#Exercise 9 - Write a Python program to insert spaces between words starting with capital letters.
def splitBySpace():
    s = input("Enter a string: ")
    x = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
    print(x)

#Exercise 10 - Write a Python program to convert a given camel case string to snake case.
def camelToSnake():
    s = input("Enter a string: ")
    x = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
    x = x.lower
    g = re.sub(r" ", r"_", x)
    print(g)

