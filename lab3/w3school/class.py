#The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class

## Create a class named MyClass:
class MyClass:
  x = 5

## Create an object of MyClass called p1:
class MyClass:
  x = 5
p1 = MyClass()
 
## Use the p1 object to print the value of x:
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

## What is the correct syntax to assign a "init" function to a class?
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
