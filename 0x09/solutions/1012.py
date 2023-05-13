# DFS
import sys
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    #--- 입력 파트 ---#
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    matrix = [[0 for col in range(M)] for row in range(N)]
    for _ in range(K):
        c, r = map(int, sys.stdin.readline().rstrip().split())
        matrix[r][c] = 1

    #--- 로직 파트 ---#
    stack = []
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                count += 1
                stack.append([i, j])
                matrix[i][j] = 0
                while stack:
                    popped = stack.pop()
                    r = popped[0]
                    c = popped[1]
                    for d in range(4):
                        dr = r + drs[d]
                        dc = c + dcs[d]
                        if 0<=dr<N and 0<=dc<M and matrix[dr][dc] == 1:
                            stack.append([dr, dc])
                            matrix[dr][dc] = 0
    #--- 출력 파트 ---#
    print(count)