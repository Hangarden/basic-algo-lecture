import sys
from collections import deque

#---입력 파트---#
M, N, H = map(int, input().split())
matrix = [[[0 for col in range(M)] for row in range(N)] for height in range(H)]
dq = deque()
for l in range(H):
    for i in range(N):
        nums = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(M):
            if nums[j] == 1:
                dq.append([l, i, j])
            matrix[l][i][j] = nums[j]

#---로직 파트---#
count = -1
dhs = [0, 0, 0, 0, -1, 1]
drs = [-1, 0, 1, 0, 0, 0]
dcs = [0, 1, 0, -1, 0, 0]
while dq:
    count += 1
    temp_dq = deque()
    while dq:
        polled = dq.popleft()
        h = polled[0]
        r = polled[1]
        c = polled[2]
        for d in range(6):
            dh = h + dhs[d]
            dr = r + drs[d]
            dc = c + dcs[d]
            if 0<=dh<H and 0<=dr<N and 0<=dc<M and matrix[dh][dr][dc] == 0:
                matrix[dh][dr][dc] = 1
                temp_dq.append([dh, dr, dc])
    dq = temp_dq

#---출력 파트---#
for l in range(H):
    for i in range(N):
        for j in range(M):
            if matrix[l][i][j] == 0:
                count = -1
                break
        if count == -1:
            break
    if count == -1:
        break
print(count)