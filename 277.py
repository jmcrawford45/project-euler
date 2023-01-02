def inverse_sentence(s: str) -> int:
    curr = 1
    for step in reversed(s):
        if step == "D":
            curr *= 3
        if step == "U":
            curr = (curr * 3 - 2) // 4
        if step == "d":
            curr = (curr * 3 + 1) // 2
    return curr

assert inverse_sentence("DdDddUUdDD") == 231
assert inverse_sentence("DdDddUUdDDDdUDUUUdDdUUDDDUdDD") == 1004064 

divisor = inverse_sentence("UDDDUdddDDUDDddDdDddDDUDDdUUDd")
print(divisor)

q, _ = divmod(10**15, divisor)
print((q+1)*divisor)
print(inverse_sentence("UD"))