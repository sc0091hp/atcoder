n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
check = False
end = False
ans = -1
for i in range(n):
    index = n - i - 1
    #存在する可能性があるかどうか
    if end == False:
        #1度でも入りきらないおもちゃがあったかどうか
        if check == False:
            if (a[index] > b[index-1]) and (index-1>=0):
                check = True
                ans = a[index]
            elif index-1 == -1:
                check = True
                ans = a[index]   
        else:
            #1度でも入りきらないおもちゃがあった上で、さらに追加で入りきらないおもちゃがあった場合
            if (a[index] > b[index]):
                end = True
                ans = -1

print(ans)