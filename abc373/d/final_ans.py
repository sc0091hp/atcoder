"""
方針   : 深さ優先探索で行う。
詳細   : 一つの頂点に書き込む値が確定すると、連結成分内すべての頂点に
         書き込むべき値が確定する。
注意点 : Pythonでは再帰回数の条件が設定されている。
        その為、再帰回数の条件値を変更する必要がある。
    　 :Atcoderへ提出する際に、Python(PyPy)ではTLEになる。
    　  その為、Python(CPython)で提出する必要がある。
再帰回数に関するURL→(https://note.nkmk.me/python-sys-recursionlimit/)
コードを書くにあたり参考にしたURL→(https://programming-hiroba.com/abc373-d/)
"""

import sys
sys.setrecursionlimit(10**6)

#baseは開始点
#一点から一点への距離
#base→スタート、tmp→隣接する辺、all_distance→距離、visit→訪問済みか否か
def dfs(base, distance):
    global visit, all_distance, tmp
    all_distance[base] = distance
    visit[base] = True
    #destionation→移動先、#part_distance→移動元から移動先の重み
    for destination, part_distance in tmp[base]:
        #移動先に訪れたことがないかどうかを確認
        if visit[destination] == False:
            all_distance[destination] = all_distance[base] + part_distance
            dfs(destination, all_distance[destination])

n, m = map(int, input().split())
#空配列を用意
tmp = []
for i in range(n):
    tmp.append([])

for i in range(m):
    u, v, w = list(map(int, input().split()))
    tmp[u-1].append([v-1, w])
    tmp[v-1].append([u-1, -w])

#頂点を訪れたかどうかを確認する為の配列を用意
visit = [False]*n

#頂点からの距離
all_distance = [0]*n
for j in range(n):
    if visit[j] == False:
    #if all_distance[j] == INF:
        #j→スタート、tmp→隣接する辺、distance→距離、visit→訪問済みか否か
        dfs(j, 0)

print(*all_distance)


    

