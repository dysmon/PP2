# ex: Write a Python program to subtract five days from current date.
import datetime

today = datetime.date.today()

five_days_ago = today - datetime.timedelta(days=5)

print("Five days ago was:", five_days_ago)