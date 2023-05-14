import sys
from collections import deque

#--- 입력 파트 ---#
N = int(input())
matrix = [['' for col in range(N)] for row in range(N)]
for i in range(N):
    s = sys.stdin.readline().rstrip()
    for j in range(N):
        matrix[i][j] = s[j]

#--- 로직 파트 ---#
def bfs(is_blind):
    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]
    visited = [[False for col in range(N)] for row in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                count += 1
                dq = deque()
                dq.append([i, j])
                visited[i][j] = True
                color = matrix[i][j]
                if is_blind and color == 'G':
                    color = 'R'
                while dq:
                    polled = dq.popleft()
                    r = polled[0]
                    c = polled[1]
                    for d in range(4):
                        dr = r + drs[d]
                        dc = c + dcs[d]
                        if 0<=dr<N and 0<=dc<N and visited[dr][dc] == False:
                            colorB = matrix[dr][dc]
                            if is_blind and colorB == 'G':
                                colorB = 'R'
                            if colorB == color:
                                dq.append([dr, dc])
                                visited[dr][dc] = True
    return count
#--- 출력 파트 ---#
print(bfs(False), end=" ")
print(bfs(True))