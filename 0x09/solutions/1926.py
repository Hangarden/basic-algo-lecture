# BFS
from collections import deque

#--- 입력 파트 ---#
N, M = map(int, input().split())
matrix= []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

#--- 로직 파트 ---#
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
count = 0
max_area = 0
dq = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            count += 1
            dq.append([i, j])
            matrix[i][j] = 0
            area = 1
            while dq:
                polled = dq.popleft()
                r = polled[0]
                c = polled[1]
                for d in range(4):
                    dr = r + drs[d]
                    dc = c + dcs[d]
                    if 0<=dr<N and 0<=dc<M and matrix[dr][dc] == 1:
                        area += 1
                        dq.append([dr, dc])
                        matrix[dr][dc] = 0
            max_area = max(max_area, area)
            
#--- 출력 파트 ---#
print(count)
print(max_area)