s = list(map(str, input()))
t = list(map(str, input()))


ans = 0
check = True
for i in range(min(len(s),len(t))):
    if s[i] != t[i] and check:
        ans = i
        check = False

if (len(s) == len(t)) and ans == 0 and s[0] != t[0]:
    print("1")
elif (len(s) == len(t)) and ans == 0:
    print("0")
elif (len(s) != len(t)) and ans == 0:
    print(min(len(s),len(t))+1)
else:
    print(ans+1)



