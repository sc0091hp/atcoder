cnt  = 0
for i in range(12):
    s = input()
    index = 0
    for j in s:
        index += 1
    if index == i+1:
        cnt += 1
print(cnt)