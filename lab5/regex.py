import re

def zeroOrMore():
    s = input("Enter a string: ")
    x = re.findall(r"ab*",s)
    print(x)

def twoOrThree():
    s = input("Enter a string: ")
    x = re.findall(r"ab{2,3}",s)
    print(x)

def sequenceOfLower():
    l = []
    s = input("Enter a string: ")
    s = s.split("_")
    for i in range(len(s)-1):
        x1 = re.search("[a-z]", s[i])
        x2 = re.search("[a-z]", s[i + 1])
        if x1 and x2:
                l.append(s[i] + "_" + s[i + 1])
    print(l)

def upperLower():
    s = input("Enter a string: ")
    x = re.findall(r"[A-Z][a-z]+",s)
    print(x)

def startAendB():
    s = input("Enter a string: ")
    x = re.findall(r"a.*b",s)
    print(x)

def replace():
    s = input("Enter a string: ")
    x = re.sub(r"[.]|[ ]|[,]",":",s)
    print(x) 

def snake_to_camel():
    s = input("Enter a string: ")
    s = s.split("_")
    if len(s)>1:
        x = s[0]
        for i in range(1, len(s)):
            x += s[i].capitalize()
        print(x)

def splitByUpper():
    s = input("Enter a string: ")
    x = re.split("[A-Z]+",s)
    print(x)

def splitBySpace():
    s = input("Enter a string: ")
    x = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
    print(x)

def camelToSnake():
    s = input("Enter a string: ")
    x = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
    x = x.lower
    g = re.sub(r" ", r"_", x)
    print(g)

