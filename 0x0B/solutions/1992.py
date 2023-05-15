import sys

#---입력 파트---#
N = int(input())
matrix = [['' for col in range(N)] for row in range(N)]
for i in range(N):
    s = sys.stdin.readline().rstrip()
    for j in range(N):
        matrix[i][j] = s[j]

#---로직 파트---#
def recursion(size, r, c):
    if size == 1:
        return matrix[r][c]
    else:
        left_top = recursion(size//2, r, c)
        right_top = recursion(size//2, r, c + size//2)
        left_bottom = recursion(size//2, r + size//2, c)
        right_bottom = recursion(size//2, r + size//2, c + size//2)
        if left_top == right_top == left_bottom == right_bottom == '0':
            return '0'
        elif left_top == right_top == left_bottom == right_bottom == '1':
            return '1'
        else:
            return '(' + left_top + right_top + left_bottom + right_bottom + ')'

#---출력 파트---#
print(recursion(N, 0, 0))