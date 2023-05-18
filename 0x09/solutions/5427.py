import sys
from collections import deque


T = int(input())
for _ in range(T):
    #---입력 파트---#
    M, N = map(int, sys.stdin.readline().rstrip().split())
    matrix = [['' for col in range(M)] for row in range(N)]

    #---로직 파트---#
    human_dq = deque()
    fire_dq = deque()
    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]
    for i in range(N):
        s = sys.stdin.readline().rstrip()
        for j in range(M):
            if s[j] == '@':
                human_dq.append([i, j])
            elif s[j] == '*':
                fire_dq.append([i, j])
            matrix[i][j] = s[j]
    count = 0
    ans = 0
    while human_dq:
        count += 1
        temp_human_dq = deque()
        temp_fire_dq = deque()
        while fire_dq:
            polled = fire_dq.popleft()
            r = polled[0]
            c = polled[1]
            for d in range(4):
                dr = r + drs[d]
                dc = c + dcs[d]
                if 0<=dr<N and 0<=dc<M and (matrix[dr][dc] == '@' or matrix[dr][dc] == '.'):
                    temp_fire_dq.append([dr, dc])
                    matrix[dr][dc] = '*'
        fire_dq = temp_fire_dq
        while human_dq:
            polled = human_dq.popleft()
            r = polled[0]
            c = polled[1]
            for d in range(4):
                dr = r + drs[d]
                dc = c + dcs[d]
                if dr<0 or dr>=N or dc<0 or dc>=M:
                    ans = count
                    temp_human_dq = deque()
                    human_dq = deque()
                    break
                if 0 <= dr < N and 0 <= dc < M and matrix[dr][dc] == '.':
                    temp_human_dq.append([dr, dc])
                    matrix[dr][dc] = '@'
        human_dq = temp_human_dq

    #---출력 파트---#
    if ans == 0:
        print("IMPOSSIBLE")
    else:
        print(ans)