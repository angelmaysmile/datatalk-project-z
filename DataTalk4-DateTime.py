# HOW TO HANDLE STRING OF TIME
from datetime import datetime
from datetime import timezone

# String of date
dt_string = "Sat 11 Aug 2018 13:54:36 -0700"

# Convert string to datetime 
dt_object = datetime.strptime(dt_string, '%a %d %b %Y %H:%M:%S %z')

print("Datetime object:", dt_object)

print("Year:", dt_object.year)
print("Month:", dt_object.month)
print("Day:", dt_object.day)
print("Convert to unixtime stamp:", dt_object.timestamp())
print("Convert to string with defined format:", dt_object.strftime('%Y-%m-%d'))

# Unix timestamp 
dt_timestamp = '1534020876'

# Convert unix timestamp to datetime
dt_object = datetime.fromtimestamp(int(dt_timestamp), timezone.utc)

print("Datetime object:", dt_object)
print("Convert to string with defined format:", dt_object.strftime('%Y-%m-%d'))