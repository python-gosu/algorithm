# 32289번: Max-Queen - <img src="https://static.solved.ac/tier_small/6.svg" style="height:20px" /> Silver V

<!-- performance -->
### 성능 요약
메모리: 32412 KB, 시간: 36 ms
<!-- end -->

## 문제

[문제 링크](https://boj.kr/32289)

<p>$n$개의 행과 $m$개의 열로 이루어진 체스판이 있습니다. 이 체스판에 퀸을 $1$개 이상 두려고 합니다.</p>

<p>여러분은 각 칸 위에 퀸을 최대 $1$개 둘 수 있습니다. 다시 말해, 각 칸에는 퀸이 $1$개 있거나 퀸이 하나도 없습니다.</p>

<p>두 퀸이 같은 행, 같은 열, 또는 같은 대각선 위에 있으며, 두 퀸 사이를 가로막는 퀸이 없을 때 두 퀸이 <strong>서로 공격할 수 있다</strong>고 합니다. 또한 퀸 $A$와 퀸 $B$가 서로 공격할 수 있을 때, 순서쌍 $(A,B)$를 <strong>공격하는 쌍</strong>이라고 합니다. 공격하는 쌍 $(A,B)$와 $(B,A)$는 같은 것으로 취급합니다.</p>

<p>예를 들어, 아래와 같이 퀸을 두면 서로 다른 공격하는 쌍이 $4$개가 됩니다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e20d526b-3a43-4af0-8ed7-38e539114b0f/-/preview/"></p>

<p style="text-align: justify;">이때 서로 다른 공격하는 쌍의 개수의 최댓값을 구하는 프로그램을 작성해 주세요.</p>

## 입력

<p>한 줄에 행의 개수 $n$과 열의 개수 $m$이 공백으로 구분되어 주어집니다. ($2 \le n,m \le 10^6$)</p>

## 출력

<p>한 줄에 문제의 정답을 출력합니다.</p>

## 소스코드

[소스코드 보기](Max-Queen.py)