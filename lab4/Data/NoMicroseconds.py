# ex:Write a Python program to drop microseconds from datetime.
import datetime

now = datetime.datetime.now()

now_without_microseconds = now.replace(microsecond=0)

print("Original date and time:", now)
print("Date and time without microseconds:", now_without_microseconds)