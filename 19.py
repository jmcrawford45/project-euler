from datetime import *

curr = date(1900, 1, 7)
count = 0
while curr <= date(2000, 12, 31):
    if curr.day == 1 and curr >= date(1901, 1, 1):
        count += 1
    curr += timedelta(days=7)
print(count)