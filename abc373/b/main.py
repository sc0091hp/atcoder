import string
en = []
number = 0
for i in string.ascii_letters:
    en.append([number, i])
    number += 1
s = input()
arr = []
index = 0
for char in s:
    for number, abcd in en:
        if abcd == char:
            arr.append([number, index])
    index += 1
arr.sort()
check = False
ans, before = 0, arr[0][1]
for char, number in arr:
    if check:
        before = number
        check = True
    else:
        ans = ans + abs(number - before)
        before = number
print(ans)