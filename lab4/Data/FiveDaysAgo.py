import datetime

today = datetime.date.today()

five_days_ago = today - datetime.timedelta(days=5)

print("Five days ago was:", five_days_ago)