import sys

#--- 입력 파트 ---#
N = int(input())
matrix = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().rstrip().split()))

#--- 로직 파트 ---#
counts = [0, 0, 0]
def recursion(size, start_row, start_col):
    if size == 1:
        ret = [0, 0, 0]  # ret: [-1의 갯수, 0의 갯수, 1의 갯수]
        ret[matrix[start_row][start_col] + 1] = 1
        return ret
    else:
        ret = [0, 0, 0]
        for i in range(3):
            for j in range(3):
                nums = recursion(size // 3, start_row + i*(size//3), start_col + j*(size//3))  # nums: [-1의 갯수, 0의 갯수, 1의 갯수]
                if nums[1] == 0 and nums[2] == 0:  # -1로만 가득 채워진 경우
                    ret[0] += 1  # -1의 갯수를 '1개'만 증가시킨다
                elif nums[0] == 0 and nums[2] == 0:  # 0으로만 가득 채워진 경우
                    ret[1] += 1  # 0의 갯수를 '1개'만 증가시킨다
                elif nums[0] == 0 and nums[1] == 0:  # 1로만 가득 채워진 경우
                    ret[2] += 1  # 1의 갯수를 '1개'만 증가시킨다
                else:  # 섞인 경우
                    ret[0] += nums[0]
                    ret[1] += nums[1]
                    ret[2] += nums[2]
        return ret

#--- 출력 파트 ---#
nums = recursion(N, 0, 0)  # nums: [-1의 갯수, 0의 갯수, 1의 갯수]
if nums[1] == 0 and nums[2] == 0:  # -1로만 가득 채워진 경우
    nums[0] = 1
elif nums[0] == 0 and nums[2] == 0:
    nums[1] = 1
elif nums[0] == 0 and nums[1] == 0:
    nums[2] = 1

for num in nums:
    print(num)