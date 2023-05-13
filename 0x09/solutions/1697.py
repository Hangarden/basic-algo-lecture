# BFS
from collections import deque

#--- 입력 파트 ---#
N, K = map(int, input().split())

#--- 로직 파트 ---#
visited = [-1] * 100001
count = 0  # 이동한 횟수
dq = deque()
dq.append(N)
visited[N] = count
while dq:
    count += 1
    temp_dq = deque()
    while dq:
        polled = dq.popleft()
        if polled == K:
            temp_dq = deque()
            break
        if polled - 1 >= 0 and visited[polled-1] == -1:
            temp_dq.append(polled-1)
            visited[polled-1] = count
        if polled + 1 <= 100000 and visited[polled+1] == -1:
            temp_dq.append(polled+1)
            visited[polled+1] = count
        if polled * 2 <= 100000 and visited[polled*2] == -1:
            temp_dq.append(polled*2)
            visited[polled*2] = count
    dq = temp_dq

#--- 출력 파트 ---#
print(count - 1)