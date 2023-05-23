from collections import deque

#--- 입력 파트 ---#
N = int(input())
matrix = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    s = input()
    for j in range(N):
        matrix[i][j] = int(s[j])

#--- 로직 파트 ---#
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
counts = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            count = 1
            dq = deque()
            dq.append([i, j])
            matrix[i][j] = 0
            while dq:
                polled = dq.popleft()
                r = polled[0]
                c = polled[1]
                for d in range(4):
                    dr = r + drs[d]
                    dc = c + dcs[d]
                    if 0<=dr<N and 0<=dc<N and matrix[dr][dc] == 1:
                        count += 1
                        dq.append([dr, dc])
                        matrix[dr][dc] = 0
            counts.append(count)

#--- 출력 파트 ---#
print(len(counts))
for count in sorted(counts):
    print(count)