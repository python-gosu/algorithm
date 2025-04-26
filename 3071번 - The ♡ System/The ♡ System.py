#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3071                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: myhouse34 <boj.kr/u/myhouse34>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3071                           #+#        #+#      #+#     #
#    Solved: 2025/04/26 15:09:03 by myhouse34     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(0)
        continue
    digits = []
    while n != 0:
        n, r = divmod(n, 3)
        if r == 2:
            digits.append('-')
            n += 1
        else:
            digits.append(str(r))

    print(''.join(reversed(digits)))
