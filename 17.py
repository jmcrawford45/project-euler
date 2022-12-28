letters = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
    ("ten", 10),
    ("eleven", 11),
    ("twelve", 12),
    ("thirteen", 13),
    ("fourteen", 14),
    ("fifteen", 15),
    ("sixteen", 16),
    ("seventeen", 17),
    ("eighteen", 18),
    ("nineteen", 19),
    ("twenty", 20),
    ("thirty", 30),
    ("forty", 40),
    ("fifty", 50),
    ("sixty", 60),
    ("seventy", 70),
    ("eighty", 80),
    ("ninety", 90),
    ("onehundred", 100),
    ("twohundred", 200),
    ("threehundred", 300),
    ("fourhundred", 400),
    ("fivehundred", 500),
    ("sixhundred", 600),
    ("sevenhundred", 700),
    ("eighthundred", 800),
    ("ninehundred", 900),
    ("onethousand", 1000),
]

def count_letters(low: int, high: int) -> int:
    count = 0
    for i in range(low, high+1):
        remainder = i
        while remainder != 0:
            for name, val in reversed(letters):
                if remainder // val == 1:
                    remainder -= val
                    if remainder and val >= 100:
                        count += len("and")
                    count += len(name)
    return count

print(count_letters(1, 1000))
