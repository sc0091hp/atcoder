max, q = list(map(int, input().split()))
left_hand = 1
right_hand = 2
f_ans = 0
ans = 0
for i in range(q):
    l = input().split()
    t = int(l[1])
    hand = l[0]
    #右手の場合
    if (hand == 'R'):
        #移動後>左>右
        if (left_hand > right_hand) and (left_hand < t):
            ans = max- (t - right_hand)
        #移動後==左>右
        elif (left_hand > right_hand) and (left_hand == t):
            #ここにくるのはありえない。
            ans = 0 
        #左>移動後>右
        elif (left_hand > right_hand) and (right_hand < t):
            ans = t - right_hand
        #左>移動後==右
        elif (left_hand > right_hand) and (right_hand == t):
            ans = 0
        #左>右>移動後
        elif (left_hand > right_hand) and (right_hand > t):
            ans = right_hand - t
        #移動後>右>左
        elif (left_hand < right_hand) and (right_hand < t):
            ans = t - right_hand
        #移動後==右>左
        elif (left_hand < right_hand) and (right_hand == t):
            ans = 0
        #右>移動後>左
        elif (left_hand < right_hand) and (left_hand < t):
            ans = right_hand - t
        #右>移動後==左
        elif (left_hand < right_hand) and (left_hand == t):
            #ここにくるのはありえない
            ans = 0
        #右>左>移動後
        elif (left_hand < right_hand) and (left_hand > t):
            ans = max- (right_hand - t)
        right_hand = t
    #左手の場合
    elif(hand == 'L'):
        #移動後>左>右
        if (left_hand > right_hand) and (left_hand < t):
            ans = t - left_hand
        #移動後==左>右
        elif (left_hand > right_hand) and (left_hand == t):
            ans = 0
        #左>移動後>右
        elif (left_hand > right_hand) and (right_hand < t):
            ans = left_hand - t
        #左>移動後==右
        elif (left_hand > right_hand) and (right_hand == t):
            #ありえない
            ans = 0
        #左>右>移動後
        elif (left_hand > right_hand) and (right_hand > t):
            ans = max- (left_hand - t)
        #移動後>右>左
        elif (left_hand < right_hand) and (right_hand < t):
            ans = max- (t- left_hand)
        #移動後==右>左
        elif (left_hand < right_hand) and (right_hand == t):
            #ありえない
            ans = 0
        #右>移動後>左
        elif (left_hand < right_hand) and (left_hand < t):
            ans = t - left_hand
        #右>移動後==左
        elif (left_hand < right_hand) and (left_hand == t):
            ans = 0
        #右>左>移動後
        elif (left_hand < right_hand) and (left_hand > t):
            ans = left_hand - t
        left_hand = t
    f_ans += ans
    ans = 0

print(f_ans)
