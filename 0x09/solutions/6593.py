from collections import deque

while True:
    #--- 입력 파트 ---#
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    matrix = [[['' for col in range(C)] for row in range(R)] for height in range(L)]
    start_height = 0
    start_row = 0
    start_col = 0
    end_height = 0
    end_row = 0
    end_col = 0
    for h in range(L):
        for i in range(R):
            s = input()
            for j in range(C):
                matrix[h][i][j] = s[j]
                if matrix[h][i][j] == 'S':
                    start_height = h
                    start_row = i
                    start_col = j
                elif matrix[h][i][j] == 'E':
                    end_height = h
                    end_row = i
                    end_col = j
            # print(matrix[h][i])
        input()

    #--- 로직 파트 ---#
    dhs = [-1, 1]
    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]
    dq = deque()
    dq.append([start_height, start_row, start_col])
    matrix[start_height][start_row][start_col] = '#'
    count = 0
    ans = -1
    while dq:
        temp_dq = deque()
        count += 1
        while dq:
            polled = dq.popleft()
            h = polled[0]
            r = polled[1]
            c = polled[2]
            if h == end_height and r == end_row and c == end_col:
                ans = count-1
                temp_dq = deque()
                break
            for d in range(2):
                dh = h + dhs[d]
                if 0<=dh<L and matrix[dh][r][c] != '#':
                    temp_dq.append([dh, r, c])
                    matrix[dh][r][c] = '#'
            for d in range(4):
                dr = r + drs[d]
                dc = c + dcs[d]
                if 0<=dr<R and 0<=dc<C and matrix[h][dr][dc] != '#':
                    temp_dq.append([h, dr, dc])
                    matrix[h][dr][dc] = '#'
        dq = temp_dq

    #--- 출력 파트 ---#
    if ans == -1:
        print("Trapped!")
    else:
        print(f'Escaped in {ans} minute(s).')