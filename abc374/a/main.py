s = list(map(str, input()))
# print(s)
index = 0
for i in s:
    index += 1

if index < 3:
    print("No")
else:
    if s[-3] == "s" and s[-2] == "a" and s[-1] == "n":
        print("Yes")
    else:
        print("No")
        