# BFS
from collections import deque

#--- 입력 파트 ---#
F, S, G, U, D = map(int, input().split())

#--- 로직 파트 ---#
dq = deque()
dq.append(S)
count = 0
ans = -99
visited = dict()
visited[S] = True
while dq:
    temp_dq = deque()
    count += 1
    while dq:
        polled = dq.popleft()
        if polled == G:
            temp_dq = deque()
            ans = count-1
            break
        else:
            if polled+U <= F and polled+U not in visited:
                temp_dq.append(polled+U)
                visited[polled+U] = True
            if polled-D >= 1 and polled-D not in visited:
                temp_dq.append(polled-D)
                visited[polled-D] = True
    dq = temp_dq

#--- 출력 파트 ---#
if ans == -99:
    print("use the stairs")
else:
    print(ans)