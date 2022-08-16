#!/usr/bin/env python3

import time
from datetime import date
import datetime
from datetime import datetime


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

today = date.today()

print(today)

e = datetime.datetime.now()

print ("Current date and time = %s" % e)

print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))

print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))


