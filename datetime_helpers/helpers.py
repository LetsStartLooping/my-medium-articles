from datetime import datetime, timedelta

# Get First day of the month for a give Date
first_day = lambda date: date.replace(day = 1)

# Last day of the month for a given date
last_day = lambda date: (date.replace(day=1) + timedelta(days=32)).replace(day=1) + timedelta(days=-1)
# Shorter Version for the same
last_day_sh = lambda date: first_day(first_day(date) + timedelta(days=32)) + timedelta(days=-1)

# Get Last day of the Previous Month for a given Date
last_day_of_prev_month = lambda date: date.replace(day = 1) + timedelta(days=-1)

# Get First day of the Previous Month for a give Date
first_day_of_prev_month = lambda date: (date.replace(day = 1) + timedelta(days=-1)).replace(day = 1)
# Shorter Version
first_day_of_prev_month_sh = lambda date: first_day(last_day_of_prev_month(date))

# Get First day of the next month
first_day_of_next_month = lambda date: (date.replace(day=1) + timedelta(days=32)).replace(day=1)

# Last Day of the next month
last_day_of_next_month = lambda date: (date.replace(day = 1) + timedelta(days = 63)).replace(day=1) + timedelta(days=-1)
# Shorter Version
last_day_of_next_month_sh = lambda date: last_day(first_day_of_next_month(date))

