#--- 입력 파트 ---#
N = int(input())

#--- 로직 파트 ---#
matrix = [[' ' for col in range(2*N-1)] for row in range(N)]
def recursion(size, r, c):
    if size == 3:
        matrix[r][c] = "*"
        matrix[r+1][c-1] = "*"
        matrix[r+1][c+1] = "*"
        for j in range(c-2, c+3):
            matrix[r+2][j] = "*"
    else:
        recursion(size//2, r, c)
        recursion(size//2, r + size//2, c-size//2)
        recursion(size//2, r + size//2, c+size//2)
recursion(N, 0, N-1)

#--- 출력 파트 ---#
for i in range(N):
    stars_line = ''.join(matrix[i])
    print(stars_line)