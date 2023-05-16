#---입력 파트---#
N = int(input())

#---로직 파트---#
matrix = [[' ' for col in range(N)] for row in range(N)]
def recursion(size, r, c):
    if size == 1:
        matrix[r][c] = "*"
    else:
        for dr in range(3):
            for dc in range(3):
                if dr != 1 or dc != 1:
                    recursion(size//3, r + dr*(size//3), c + dc*(size//3))

#---출력 파트---#
recursion(N, 0, 0)
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end="")
    print()