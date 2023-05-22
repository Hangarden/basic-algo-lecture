#--- 입력 파트 ---#
N = int(input())
matrix = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    matrix[i] = list(map(int, input().split()))

#--- 로직 파트 ---#
def move_up(temp_matrix):
    merged = [[False for col in range(N)] for row in range(N)]
    for j in range(N):
        for i in range(N):
            if temp_matrix[i][j] == 0: continue
            r = i
            while r-1>=0:
                if temp_matrix[r-1][j] == 0:
                    temp_matrix[r-1][j] = temp_matrix[r][j]
                    temp_matrix[r][j] = 0
                    r -= 1
                elif temp_matrix[r-1][j] == temp_matrix[r][j]:
                    if merged[r-1][j]:
                        break
                    else:
                        temp_matrix[r-1][j] = temp_matrix[r][j] * 2
                        merged[r-1][j] = True
                        temp_matrix[r][j] = 0
                        r -= 1
                        break
                else:
                    break


def move_down(temp_matrix):
    merged = [[False for col in range(N)] for row in range(N)]
    for j in range(N):
        for i in range(N-1, -1, -1):
            if temp_matrix[i][j] == 0: continue
            r = i
            while r+1<N:
                if temp_matrix[r+1][j] == 0:
                    temp_matrix[r+1][j] = temp_matrix[r][j]
                    temp_matrix[r][j] = 0
                    r += 1
                elif temp_matrix[r+1][j] == temp_matrix[r][j]:
                    if merged[r+1][j]:
                        break
                    else:
                        temp_matrix[r+1][j] = temp_matrix[r][j] * 2
                        merged[r+1][j] = True
                        temp_matrix[r][j] = 0
                        r += 1
                        break
                else:
                    break

def move_left(temp_matrix):
    merged = [[False for col in range(N)] for row in range(N)]
    for i in range(N):
        for j in range(N):
            if temp_matrix[i][j] == 0: continue
            c = j
            while c-1>=0:
                if temp_matrix[i][c-1] == 0:
                    temp_matrix[i][c-1] = temp_matrix[i][c]
                    temp_matrix[i][c] = 0
                    c -= 1
                elif temp_matrix[i][c-1] == temp_matrix[i][c]:
                    if merged[i][c-1]:
                        break
                    else:
                        temp_matrix[i][c-1] = temp_matrix[i][c] * 2
                        merged[i][c-1] = True
                        temp_matrix[i][c] = 0
                        c -= 1
                        break
                else:
                    break

def move_right(temp_matrix):
    merged = [[False for col in range(N)] for row in range(N)]
    for i in range(N):
        for j in range(N-1, -1, -1):
            if temp_matrix[i][j] == 0: continue
            c = j
            while c+1<N:
                if temp_matrix[i][c+1] == 0:
                    temp_matrix[i][c+1] = temp_matrix[i][c]
                    temp_matrix[i][c] = 0
                    c += 1
                elif temp_matrix[i][c+1] == temp_matrix[i][c]:
                    if merged[i][c+1]:
                        break
                    else:
                        temp_matrix[i][c+1] = temp_matrix[i][c] * 2
                        merged[i][c+1] = True
                        temp_matrix[i][c] = 0
                        c += 1
                        break
                else:
                    break

def recursion(commands):
    if len(commands) == 5:
        temp_matrix = [[0 for col in range(N)] for row in range(N)]
        for i in range(N):
            for j in range(N):
                temp_matrix[i][j] = matrix[i][j]
        for command in commands:
            if command == "U":
                move_up(temp_matrix)
            elif command == "D":
                move_down(temp_matrix)
            elif command == "L":
                move_left(temp_matrix)
            elif command == "R":
                move_right(temp_matrix)

        # print(commands)
        max_num = 0
        for i in range(N):
            for j in range(N):
                max_num = max(max_num, temp_matrix[i][j])
        #         print(temp_matrix[i][j], end=" ")
        #     print()
        # print("-----------")
        return max_num
    else:
        max_num = 0
        max_num = max(max_num, recursion((commands + "U")))
        max_num = max(max_num, recursion((commands + "D")))
        max_num = max(max_num, recursion((commands + "L")))
        max_num = max(max_num, recursion((commands + "R")))
        return max_num

#--- 출력 파트 ---#
print(recursion(""))