import sys
from collections import deque

#---입력 파트---#
N, M, K = map(int, input().split())
matrix = [[0 for col in range(M)] for row in range(N)]
for _ in range(K):
    j1, i1, j2, i2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(i1, i2):
        for j in range(j1, j2):
            matrix[i][j] = 1

#---로직 파트---#
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
count = 0
ans = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            count += 1
            dq = deque()
            dq.append([i, j])
            matrix[i][j] = 1
            area = 1
            while dq:
                polled = dq.popleft()
                r = polled[0]
                c = polled[1]
                for d in range(4):
                    dr = r + drs[d]
                    dc = c + dcs[d]
                    if 0<=dr<N and 0<=dc<M and matrix[dr][dc] == 0:
                        dq.append([dr, dc])
                        matrix[dr][dc] = 1
                        area += 1
            ans.append(area)

#---출력 파트---#
print(count)
for num in sorted(ans):
    print(num, end=" ")