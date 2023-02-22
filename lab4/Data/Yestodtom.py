import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)

print("Yesterday's date:", yesterday)
print("Today's date:", today)
print("Tomorrow's date:", tomorrow)