# Date & Time in Python

from datetime import datetime, timedelta

# ----------------------------------
# Current Date & Time
# ----------------------------------

now = datetime.now()

print("Current Date & Time :", now)
print("Date               :", now.date())
print("Time               :", now.time())

print("Year               :", now.year)
print("Month              :", now.month)
print("Day                :", now.day)

print("Hour               :", now.hour)
print("Minute             :", now.minute)
print("Second             :", now.second)

print("Weekday (0-6)      :", now.weekday())      # Monday = 0
print("Weekday Name       :", now.strftime("%A")) # Saturday

# ----------------------------------
# Date Formatting (strftime)
# ----------------------------------

from datetime import datetime, timedelta

print(now.strftime("%d-%m-%Y"))          # 04-07-2026
print(now.strftime("%d/%m/%Y"))          # 04/07/2026
print(now.strftime("%A"))                # Saturday
print(now.strftime("%B"))                # July
print(now.strftime("%I:%M %p"))          # 02:30 PM
print(now.strftime("%H:%M:%S"))          # 14:30:45

# ----------------------------------
# String to Datetime (strptime)
# ----------------------------------

from datetime import datetime, timedelta

date = "04-07-2026"

converted_date = datetime.strptime(date, "%d-%m-%Y")

print(converted_date)

# ----------------------------------
# timedelta
# ----------------------------------

from datetime import datetime, timedelta
today = datetime.now()

future_7_days = today + timedelta(days=7)
past_30_days = today - timedelta(days=30)

print("Today       :", today)
print("After 7 Days:", future_7_days)
print("Past 30 Days:", past_30_days)