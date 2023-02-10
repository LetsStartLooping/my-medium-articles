from datetime import datetime, timedelta

# Create a date/time object
date_time = datetime(year=2022, month=1, day=14, hour=15, minute=30, second=24)
print(date_time)

# Add two days
date_time = date_time + timedelta(days=2)
print("Date after adding 2 days: ", date_time)

#------------------------------#
# OUTPUT:
#------------------------------#

# 2022-01-14 15:30:24
# Date after adding 2 days:  2022-01-16 15:30:24

