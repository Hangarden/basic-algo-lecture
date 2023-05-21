import sys

#--- 입력 파트 ---#
N, M, K = map(int, input().split())
matrix=[[0 for col in range(M)] for row in range(N)]

#--- 로직 파트 ---#
for _ in range(K):
    R, C = map(int, sys.stdin.readline().rstrip().split())
    sticker_0 = [[0 for col in range(C)] for row in range(R)]
    sticker_90 = [[0 for col in range(R)] for row in range(C)]
    sticker_180 = [[0 for col in range(C)] for row in range(R)]
    sticker_270 = [[0 for col in range(R)] for row in range(C)]
    for i in range(R):
        sticker_0[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    # 90도 회전
    for i in range(C):
        for j in range(R):
            sticker_90[i][j] = sticker_0[R-1-j][i]

    # 180도 회전
    for i in range(R):
        for j in range(C):
            sticker_180[i][j] = sticker_90[C-1-j][i]

    # 270도 회전
    for i in range(C):
        for j in range(R):
            sticker_270[i][j] = sticker_180[R-1-j][i]

    stickers = [sticker_0, sticker_90, sticker_180, sticker_270]
    is_applied = False  # 현재 스티커가 부착되었는지 여부 판별하는 플래그
    for d in range(4):
        if is_applied: break
        sticker = stickers[d]
        width = len(sticker[0])
        height = len(sticker)
        for i in range(N):
            if is_applied: break
            for j in range(M):
                if width <= M-j and height <= N-i:  # 스티커의 너비나 높이가 부착 가능한너비와 높이인지를 먼저 따져본다
                    flag = False  # 현재 스티커가 부착 불가능한지 여부 판별하는 플래그
                    for k in range(height):
                        for l in range(width):
                            if sticker[k][l] == 1 and matrix[i+k][j+l] != 0:
                                flag = True
                                break
                    if not flag:
                        # 스티커 부착한다
                        for k in range(height):
                            for l in range(width):
                                if sticker[k][l] == 1 and matrix[i+k][j+l] == 0:
                                    matrix[i+k][j+l] = 1
                        is_applied = True
                        break
#--- 출력 파트 ---#
count = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            count += 1
print(count)