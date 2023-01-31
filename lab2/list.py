# List is a collection which is ordered and changeable. Allows duplicate members

fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# banana

fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'
# ["kiwi", "banana", "cherry"]

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
# ["apple", "banana", "cherry", "orange"]

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
# ["apple", "lemon", "banana", "orange"]

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
# "apple", "cherry"]

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
# cherry

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
# ["cherry", "orange", "kiwi"]

fruits = ["apple", "banana", "cherry"]
print(len(fruits))
# [3]