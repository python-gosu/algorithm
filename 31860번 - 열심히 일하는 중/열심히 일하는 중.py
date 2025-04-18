#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 31860                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: myhouse34 <boj.kr/u/myhouse34>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/31860                          #+#        #+#      #+#     #
#    Solved: 2025/04/18 21:59:00 by myhouse34     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
우선순위 큐 쓰면 될 듯.
"""
import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split(' '))

heap = []

for _ in range(N):
    heapq.heappush(heap, -int(input()))

answers = []
satisfaction = 0
while heap:
    peek = -heap[0]
    if peek <= K:
        break
    
    done_task = -heapq.heappop(heap)
    satisfaction = (satisfaction // 2) + done_task
    new_d = done_task - M
    answers.append(satisfaction)
    heapq.heappush(heap, -new_d)


print(len(answers))
for n in answers:
    print(n)
