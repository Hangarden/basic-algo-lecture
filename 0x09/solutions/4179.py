import sys
from collections import deque

#--- 입력 파트 ---#
N, M = map(int, input().split())
matrix = [['' for col in range(M)] for row in range(N)]
jdq = deque()
fdq = deque()

for i in range(N):
    s = sys.stdin.readline().rstrip()
    for j in range(M):
        matrix[i][j] = s[j]
        if matrix[i][j] == 'J':
            jdq.append([i, j])
        elif matrix[i][j] == 'F':
            fdq.append([i, j])

#---로직 파트 ---#
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
time = 0
ans = -1
while jdq:
    time += 1
    temp_jdq = deque()
    temp_fdq = deque()
    while fdq:
        polled = fdq.popleft()
        r = polled[0]
        c = polled[1]
        for d in range(4):
            dr = r + drs[d]
            dc = c + dcs[d]
            if 0 <= dr < N and 0 <= dc < M and (matrix[dr][dc] == 'J' or matrix[dr][dc] == '.'):
                matrix[dr][dc] = 'F'
                temp_fdq.append([dr,dc])
    fdq = temp_fdq
    while jdq:
        polled = jdq.popleft()
        r = polled[0]
        c = polled[1]
        for d in range(4):
            dr = r + drs[d]
            dc = c + dcs[d]
            if 0 <= dr < N and 0 <= dc < M:
                if matrix[dr][dc] == '.':
                    matrix[dr][dc] = 'J'
                    temp_jdq.append([dr, dc])
            else:
                ans = time
                break
    if ans > 0:
        break
    jdq = temp_jdq

#---출력 파트 ---#
if ans == -1:
    print('IMPOSSIBLE')
else:
    print(ans)