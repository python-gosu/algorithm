#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 23322                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: myhouse34 <boj.kr/u/myhouse34>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/23322                          #+#        #+#      #+#     #
#    Solved: 2025/05/05 14:04:45 by myhouse34     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def calc(arr):
    day = 0
    cnt = 0
    min_val = min(arr)
    for i in range(1, len(arr)):
        if arr[i - 1] <= arr[i] and min_val < arr[i]:
            while arr[i] > arr[i - 1]:
                arr[i] -= 1
                cnt += 1
            day += 1
    print(cnt, day)

N, K = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
calc(sorted(arr))