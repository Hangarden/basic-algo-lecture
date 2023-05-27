# 2048(easy) 문제에서 한쪽 방향으로 숫자를 밀어넣는 방법을 익혔다면 쉽게 풀리는 문제이다
from collections import deque

#--- 입력 파트 ---#
matrix = [['.' for col in range(6)] for row in range(12)]

for i in range(12):
    s = input()
    for j in range(6):
        matrix[i][j] = s[j]

#--- 로직 파트 ---#
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
def is_chaining(start_row, start_col, matrix):
    temp_matrix = [['.' for col in range(6)] for row in range(12)]
    temp_visited = [[False for col in range(6)] for row in range(12)]

    # matrix 복사
    for i in range(12):
        for j in range(6):
            temp_matrix[i][j] = matrix[i][j]
    dq = deque()  # 덱 선언
    color = matrix[start_row][start_col]  # 시작하는 뿌요의 색상 저장
    dq.append([start_row, start_col])  # 시작하는 뿌요의 좌표 추가
    temp_visited[start_row][start_col] = True  # 방문처리
    temp_matrix[start_row][start_col] = "."  # 방문한 뿌요는 터트린다
    count = 1  # 1개 터졌으므로 카운트 추가
    while dq:  # BFS 돌리며 인접한 뿌요들 일단 터트려본다
        polled = dq.popleft()
        r = polled[0]
        c = polled[1]
        for d in range(4):
            dr = r + drs[d]
            dc = c + dcs[d]
            if 0<=dr<12 and 0<=dc<6 and temp_matrix[dr][dc] == color and temp_visited[dr][dc] == False:
                dq.append([dr, dc])
                temp_matrix[dr][dc] = "."
                temp_visited[dr][dc] = True
                count += 1
    if count >= 4:  # 터진 뿌요가 4개 이상이라면 연쇄가 발생한 것이다
        for i in range(12):
            for j in range(6):
                matrix[i][j] = temp_matrix[i][j]  # 원본 matrix 업데이트
        return True
    else:
        return False

count = 0
is_puyo = True  # 연쇄가 단 한번이라도 발생하였는지 여부를 판단하는 플래그 변수
while is_puyo:
    is_puyo = False
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.':
                is_puyo = is_chaining(i, j, matrix) or is_puyo  # 연쇄가 단 한번이라도 발생되었다면 is_puyo는 계속해서 True로 세팅된다
    if is_puyo:  # 연쇄 반응이 일어났다면
        count += 1  # 연쇄 카운트 하나 늘리고
        for j in range(6):  # 내리기 작업한다. 이때 O(n)이 걸리게끔 알고리즘을 작성해야 한다
            start_index = -1  # (삽질 포인트) start_index의 초기값을 -1로 설정해주어야만 했다. 그러지 않고 0으로 잡아주다보니, 실제로 빈칸이 없는 뿌요들로 가득찬 열의 경우에도 마지막 한 칸을 비워버리게 되었다
            for i in range(11, -1, -1):
                if matrix[i][j] == ".":
                    start_index = i  # 빈칸 발견하면 시작 인덱스 업데이트하고
                    break  # 루프문 빠져나온다
            idx = start_index  # idx: 빈칸을 가리키는 인덱스
            for i in range(start_index, -1, -1):
                if matrix[i][j] != ".":  # 빈칸이 아닌 뿌요가 발견되었다면
                    matrix[idx][j] = matrix[i][j]  # 현재 idx가 가리키는 빈칸을 뿌요로 채운다
                    matrix[i][j] = "."  # 기존의 뿌요는 빈칸으로 업데이트
                    idx -= 1  # (핵심)채워진 빈칸의 다음에는 무조건 빈칸이다
        # 디버깅용 코드
        # for i in range(12):
        #     print(matrix[i])
        # print()
    else:
        break

#--- 출력 파트 ---#
print(count)