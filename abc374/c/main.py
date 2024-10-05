
n = int(input())
k = list(map(int, input().split()))


import itertools
t = list(itertools.product([0, 1], repeat=n))

ans = 20*(10**8) + 1
for i in t:
    index = 0
    group_a = 0
    group_b = 0
    count_a = 0
    count_b = 0
    
    for j in i:
        if j == 0:
            group_a += k[index]
            count_a += 1
        else:
            group_b += k[index]
            count_b += 1
        index += 1
    if count_a != 0 and count_b != 0:
        tmp = max(group_a, group_b)
        ans = min(ans, tmp)
        
print(ans)
