#!/usr/bin/env python3

from datetime import date
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

today = date.today()
print(today, end=" ")

print(current_time)
