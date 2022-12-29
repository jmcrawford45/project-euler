curr = 1
from collections import Counter
while True:
    if all(Counter(str(curr)) == Counter(str(curr*i)) for i in range(2,7)):
        print(curr)
        break
    curr += 1