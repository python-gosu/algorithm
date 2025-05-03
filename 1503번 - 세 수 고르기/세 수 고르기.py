#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1503                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: myhouse34 <boj.kr/u/myhouse34>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1503                           #+#        #+#      #+#     #
#    Solved: 2025/05/03 13:31:44 by myhouse34     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
S = list(map(int, input().split()))

answer = 10e9

for i in range(1, 1002):
    if i in S:
        continue
    for j in range(1, 1002):
        if j in S:
            continue
        for k in range(1, 1002):
            if k in S:
                continue
            q = (i * j * k)
            if abs(N - q) < answer:
                answer = abs(N - q)
            if N + 1 < q:
                break

print(answer)