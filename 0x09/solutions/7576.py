from collections import deque

#--- 입력 파트 ---#
M, N = map(int, input().split())
matrix = [[0 for col in range(M)] for row in range(N)]
dq = deque()
for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(M):
        matrix[i][j] = nums[j]
        if matrix[i][j] == 1:
            dq.append([i, j])

#--- 로직 파트 ---#
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
count = -1
while dq:
    temp_dq = deque()
    count += 1
    while dq:
        polled = dq.popleft()
        r = polled[0]
        c = polled[1]
        for d in range(4):
            dr = r + drs[d]
            dc = c + dcs[d]
            if 0<=dr<N and 0<=dc<M and matrix[dr][dc] == 0:
                temp_dq.append([dr, dc])
                matrix[dr][dc] = 1
    dq = temp_dq

#--- 출력 파트 ---#
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            count = -1
            break
    if count == -1:
        break
print(count)