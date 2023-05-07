# DFS
from collections import deque

#--- 입력 파트 ---#
N, M = map(int, input().split())
matrix = [[0 for col in range(M)] for row in range(N)]
for i in range(N):
    s = input()
    for j in range(M):
        matrix[i][j] = int(s[j])

#--- 로직 파트 ---#
dq = deque()
dq.append([0,0])
matrix[0][0] = 0
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
length = 0
while dq:
    length += 1
    temp_dq = deque()
    while dq:
        polled = dq.popleft()
        r = polled[0]
        c = polled[1]
        if r == N-1 and c == M-1:
            temp_dq = deque()
            break
        for d in range(4):
            dr = r + drs[d]
            dc = c + dcs[d]
            if 0<=dr<N and 0<=dc<M and matrix[dr][dc] == 1:
                temp_dq.append([dr, dc])
                matrix[dr][dc] = 0
    dq = temp_dq

#--- 출력 파트 ---#
print(length)