#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2822                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: myhouse34 <boj.kr/u/myhouse34>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2822                           #+#        #+#      #+#     #
#    Solved: 2025/04/16 21:03:24 by myhouse34     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
두 가지 정렬 조건을 가지고 정렬을 하면 됨.
점수 기준
기본순서 기준
"""
arr = [
    (i+1, int(input())) for i in range(8)
]

arr.sort(key=lambda x: x[1], reverse=True)
result = sorted(arr[:5], key=lambda x: x[0])

print(sum(list(map(lambda x: x[1], result))))
print(" ".join(list(map(lambda x: str(x[0]), result))))
