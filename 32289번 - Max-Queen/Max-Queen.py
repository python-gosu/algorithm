#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 32289                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: myhouse34 <boj.kr/u/myhouse34>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/32289                          #+#        #+#      #+#     #
#    Solved: 2025/04/17 22:07:55 by myhouse34     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
print(4 * n * m - 3 * (n + m) + 2)
