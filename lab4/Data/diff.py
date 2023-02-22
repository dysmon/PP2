import datetime

# Define the two dates
date1 = datetime.datetime(2023, 2, 20, 12, 0, 0)
date2 = datetime.datetime(2023, 2, 21, 13, 0, 0)

# Calculate the difference in seconds
difference_in_seconds = (date2 - date1).total_seconds()

# Print the difference
print("Difference in seconds:", difference_in_seconds)