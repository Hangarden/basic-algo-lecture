# 시간 복잡도 O(N * logL)
# pypy3로 제출해야만 통과됨. 최적화 하거나 다른 알고리즘을 사용해야만 한다

import sys
from collections import deque
import heapq

#--- 입력 파트 ---#
N, L = map(int, input().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
ans = [0] * N

#--- 로직 파트 ---#
min_num = 9999999999
dq = deque()  # 슬라이딩 윈도우
dic = dict()  # dic[num]: 슬라이딩 윈도우 내에 num이 몇 개 있는지 세는 용도
h = []  # 최소 힙
for i in range(N):
    num = nums[i]
    dq.append(num)
    heapq.heappush(h, num)
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
    left = i - L + 1
    if left > 0:
        polled = dq.popleft()
        dic[polled] -= 1
        if dic[polled] == 0:
            del dic[polled]

    # (핵심)슬라이딩 윈도우 내에서 최소값 찾기
    while h:
        if h[0] in dic:  # 최소값이 슬라이딩 윈도우 내에 존재한다면
            min_num = h[0]  # 최소값 업데이트 한다
            break
        else:
            heapq.heappop(h)

    ans[i] = min_num

#--- 출력 파트 ---#
for n in ans:
    print(n, end=" ")