n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

tmp = 1
for i in range(1,n+1):
    if(tmp >= i):
        tmp = arr[tmp-1][i-1]
    else:
        tmp = arr[i-1][tmp-1]
    
print(tmp)