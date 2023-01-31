# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
# True 

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
# {"apple", "banana", "cherry" ,"orange"}

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
# {"apple", "banana", "cherry", "orange", "mango", "grapes"}

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
# {"apple", "cherry"}  If the item to remove does not exist, remove() will raise an error.

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
# {"apple", "cherry"}  If the item to remove does not exist, discard() will NOT raise an error. 

