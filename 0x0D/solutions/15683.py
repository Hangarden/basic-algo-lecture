# 5번 CCTV는 회전할 필요가 없기 때문에 미리 matrix에서 감시 지역을 칠해도 좋다(하지만 코드가 지저분해지므로 여기서는 생략하였다)
#--- 입력 파트 ---#
N, M = map(int, input().split())
matrix = [[0 for col in range(M)] for row in range(N)]
cctvs = []
for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(M):
        matrix[i][j] = nums[j]
        if 1<= matrix[i][j] <= 5:
            cctvs.append([i, j, nums[j]])

#--- 로직 파트 ---#
min_count = 9999999999
def rotate(index, directions):
    if index == len(cctvs):
        # 원본 matrix 복사
        temp_matrix = [[0 for col in range(M)] for row in range(N)]
        for i in range(N):
            for j in range(M):
                temp_matrix[i][j] = matrix[i][j]

        # cctv의 방향에 맞추어 감시지역을 9로 칠한다
        for n in range(len(cctvs)):
            cctv = cctvs[n]
            r = cctv[0]
            c = cctv[1]
            direction = directions[n]
            for d in direction:
                if d == "R":
                    for j in range(c+1, M):
                        if temp_matrix[r][j] == 6:
                            break
                        else:
                            temp_matrix[r][j] = 9
                elif d == "L":
                    for j in range(c-1, -1, -1):
                        if temp_matrix[r][j] == 6:
                            break
                        else:
                            temp_matrix[r][j] = 9
                elif d == "T":
                    for i in range(r-1, -1, -1):
                        if temp_matrix[i][c] == 6:
                            break
                        else:
                            temp_matrix[i][c] = 9
                elif d == "B":
                    for i in range(r+1, N):
                        if temp_matrix[i][c] == 6:
                            break
                        else:
                            temp_matrix[i][c] = 9
        # 사각지대 계산
        count = 0
        for i in range(N):
            for j in range(M):
                if temp_matrix[i][j] == 0:
                    count += 1
        global min_count
        min_count = min(min_count, count)
    else:
        cctv_num = cctvs[index][2]
        if cctv_num == 1:
            rotate(index+1, directions + [["R"]])
            rotate(index+1, directions + [["B"]])
            rotate(index+1, directions + [["L"]])
            rotate(index+1, directions + [["T"]])
        elif cctv_num == 2:
            rotate(index+1, directions + [["R", "L"]])
            rotate(index+1, directions + [["T", "B"]])
        elif cctv_num == 3:
            rotate(index+1, directions + [["T", "R"]])
            rotate(index+1, directions + [["R", "B"]])
            rotate(index+1, directions + [["B", "L"]])
            rotate(index+1, directions + [["L", "T"]])
        elif cctv_num == 4:
            rotate(index + 1, directions + [["L", "T", "R"]])
            rotate(index + 1, directions + [["T", "R", "B"]])
            rotate(index + 1, directions + [["R", "B", "L"]])
            rotate(index + 1, directions + [["B", "L", "T"]])
        elif cctv_num == 5:
            rotate(index + 1, directions + [["T", "R", "B", "L"]])

rotate(0, [])

#--- 출력 파트 ---#
print(min_count)