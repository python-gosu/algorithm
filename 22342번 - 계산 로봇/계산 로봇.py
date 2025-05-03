#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 22342                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: myhouse34 <boj.kr/u/myhouse34>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/22342                          #+#        #+#      #+#     #
#    Solved: 2025/04/29 22:49:40 by myhouse34     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(M)]

dp = [[0] * N for _ in range(M)]
for i in range(M):
    dp[i][0] = arr[i][0]

result = 0
for j in range(1, N):
    for i in range(M):
        mx = 0
        for k in (-1, 0, 1):
            ni = i + k
            if 0 <= ni < M:
                mx = max(mx, dp[ni][j - 1])
        dp[i][j] = mx + arr[i][j]
        result = max(result, mx)

print(result)
