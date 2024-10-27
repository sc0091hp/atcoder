n, c = list(map(int, input().split()))
t = list(map(int, input().split()))

check = False
ans = 0
for time in t:
    if check == False:
        ans += 1
        check = True
        before_time = time
    else:
        if time - before_time >= c:
            ans += 1
            before_time = time
    
print(ans)