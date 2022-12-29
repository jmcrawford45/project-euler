curr_num, curr_denom = 1,2
res = 0
for i in range(1, 1000):
    if len(str(curr_denom + curr_num)) > len(str(curr_denom)):
        res += 1
    tmp_denom = curr_denom
    curr_denom += curr_denom+curr_num
    curr_num = tmp_denom
print(res)
