#--- 입력 파트 ---#
matrix = [[0 for col in range(8)] for row in range(4)]
for i in range(4):
    s = input()
    for j in range(8):
        matrix[i][j] = int(s[j])
K = int(input())

#--- 로직 파트 ---#
for _ in range(K):
    n, d = map(int, input().split())
    n -= 1
    spin_directions = [0, 0, 0, 0]  # 0: 회전하지 않음, 1: 시계방향 회전, -1: 반시계방향 회전
    spin_directions[n] = d

    # 회전시킨 톱니 기준 왼쪽 톱니들의 회전 방향을 계산
    for i in range(n-1, -1, -1):
        if matrix[i][2] != matrix[i+1][6]:
            spin_directions[i] = -1 * spin_directions[i+1]
    # 회전시킨 톱니 기준 오른쪽 톱니들의 회전 방향을 계산
    for i in range(n+1, 4):
        if matrix[i][6] != matrix[i-1][2]:
            spin_directions[i] = -1 * spin_directions[i-1]
    # 회전시키기
    for i in range(4):
        if spin_directions[i] == -1:
            matrix[i].append(matrix[i].pop(0))
        elif spin_directions[i] == 1:
            matrix[i].insert(0, matrix[i].pop())

#--- 출력 파트 ---#
summation = 0
for i in range(4):
    summation += matrix[i][0] * 2**i
print(summation)