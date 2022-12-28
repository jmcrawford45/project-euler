double_palindromes = set()
for i in range(1_000_000):
    num = i+1
    if str(num) == ''.join(reversed(str(num))) and bin(num)[2:] == ''.join(reversed(bin(num)[2:])):
        double_palindromes.add(num)
print(sum(double_palindromes))
