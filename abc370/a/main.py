l, r = list(map(int, input().split()))
ans = ["Yes","No","Invalid"]
if (l == 1) and (r == 0):
    print(ans[0])
elif (l == 0) and (r == 1):
    print(ans[1])
else:
    print(ans[2])
