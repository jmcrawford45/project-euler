def is_palindrome(n: int) -> bool:
    return int(''.join(reversed(str(n)))) == n

def is_lychrel(n: int) -> bool:
    curr = n
    for _ in range(50):
        curr = curr + int(''.join(reversed(str(curr))))
        if is_palindrome(curr):
            return False
    return True

assert not is_lychrel(349)
assert is_lychrel(196)

print(len([i for i in range(10_000) if is_lychrel(i)]))

