#--- 입력 파트 ---#
N, M, r, c, K = map(int, input().split())
matrix = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    matrix[i] = list(map(int, input().split()))
orders = list(map(int, input().split()))

#--- 로직 파트 ---#
dice_garo = [0, 0, 0, 0]  # 주사위를 위에서 바라보았을 때 가로에 있는 숫자들(0: 맨 윗면, 2: 맨 아랫면)
dice_sero = [0, 0, 0, 0]  # 주사위를 위에서 바라보았을 때 세로에 있는 숫자들(0: 맨 윗면, 2: 맨 아랫면)
for order in orders:
    if order == 1 and c+1 < M:
        c += 1
        dice_garo.insert(0, dice_garo.pop())  # 동쪽으로 굴린다
        dice_sero[0] = dice_garo[0]  # 윗면 일치시키기
        dice_sero[2] = dice_garo[2]  # 아랫면 일치시키기
    elif order == 2 and c-1 >= 0:
        c -= 1
        dice_garo.append(dice_garo.pop(0))  # 서쪽으로 굴린다
        dice_sero[0] = dice_garo[0]
        dice_sero[2] = dice_garo[2]
    elif order == 3 and r-1 >= 0:
        r -= 1
        dice_sero.append(dice_sero.pop(0))  # 남쪽으로 굴린다
        dice_garo[0] = dice_sero[0]
        dice_garo[2] = dice_sero[2]
    elif order == 4 and r+1 < N:
        r += 1
        dice_sero.insert(0, dice_sero.pop())  # 북쪽으로 굴린다
        dice_garo[0] = dice_sero[0]
        dice_garo[2] = dice_sero[2]
    else:
        continue
    if matrix[r][c] == 0:  # 지도에 적힌 숫자가 0이라면
        matrix[r][c] = dice_garo[2]  # 주사위 아랫면을 복사한다
    else:
        dice_sero[2] = matrix[r][c]  # 지도에 적힌 숫자를 아랫면에 복사한다
        dice_garo[2] = matrix[r][c]
        matrix[r][c] = 0  # 지도에 적힌 숫자는 0으로 만들기

    #--- 출력 파트 ---#
    print(dice_sero[0])

"""
dice_garo = [1, 3, 6, 4]
dice_sero = [1, 2, 6, 5]

동쪽
dice_garo = [4, 1, 3, 6]
dice_sero = [4, 2, 3, 5]

서쪽
dice_garo = [3, 6, 4, 1]
dice_sero = [3, 2, 4, 5]

남쪽
dice_garo = [2, 3, 5, 4]
dice_sero = [2, 6, 5, 1]

북쪽
dice_garo = [5, 3, 2, 4]
dice_sero = [5, 1, 2, 6]
"""