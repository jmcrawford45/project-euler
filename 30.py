res = 0
for i in range(10, 5*9**5):  # since 10^5 < 6 * 9^5 < 10^6
    if sum(int(c)**5 for c in str(i)) == i:
        res += i
print(res)
