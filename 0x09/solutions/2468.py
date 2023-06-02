from collections import deque

#--- 입력 파트 ---#
N = int(input())
matrix =[[0 for col in range(N)] for row in range(N)]
for i in range(N):
    matrix[i] = list(map(int, input().split()))

#--- 로직 파트 ---#
max_count = 0
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
for height in range(101):  # 왜 0인 경우를 포함해야만 하는것이지?? 비가 오는 상황만을 가정해야하므로 비의 높이가 0인 경우를 생각하면 안되는 것 아닌가??
    visited = [[False for col in range(N)] for row in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > height and visited[i][j] == False:
                count += 1
                visited[i][j] = True
                dq = deque()
                dq.append([i, j])
                visited[i][j] = True
                while dq:
                    polled = dq.popleft()
                    r = polled[0]
                    c = polled[1]
                    for d in range(4):
                        dr = r + drs[d]
                        dc = c + dcs[d]
                        if 0<=dr<N and 0<=dc<N and matrix[dr][dc] > height and visited[dr][dc] == False:
                            dq.append([dr, dc])
                            visited[dr][dc] = True
    max_count = max(max_count, count)
    if max_count == 0: break

#--- 출력 파트 ---#
print(max_count)