from collections import deque

T = int(input())

drs = [-1, -2, -2, -1, 1, 2, 2, 1]
dcs = [-2, -1, 1, 2, 2, 1, -1, -2]
for _ in range(T):
    #---입력 파트---#
    N = int(input())
    knight = list(map(int, input().split()))
    target = list(map(int, input().split()))

    #---로직 파트---#
    visited = [[False for col in range(N)] for row in range(N)]
    dq = deque()
    dq.append(knight)
    visited[knight[0]][knight[1]] = True
    count = -1
    while dq:
        count += 1
        temp_dq = deque()
        while dq:
            polled = dq.popleft()
            if polled == target:
                temp_dq = deque()
                break
            r = polled[0]
            c = polled[1]
            for d in range(8):
                dr = r + drs[d]
                dc = c + dcs[d]
                if 0<=dr<N and 0<=dc<N and visited[dr][dc] == False:
                    temp_dq.append([dr, dc])
                    visited[dr][dc] = True
        dq = temp_dq

    #---출력 파트---#
    print(count)