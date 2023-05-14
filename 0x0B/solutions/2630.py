import sys

#--- 입력 파트 ---#
N = int(input())
matrix = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().rstrip().split()))

#--- 로직 파트 ---#
def recursion(size, start_row, start_col):
    if size == 1:
        ret = [0, 0]
        ret[matrix[start_row][start_col]] = 1
        return ret
    else:
        ret = [0, 0]
        for dr in range(2):
            for dc in range(2):
                nums = recursion(size // 2, start_row + dr*(size//2), start_col + dc*(size//2))
                if nums[1] == 0:
                    ret[0] += 1
                elif nums[0] == 0:
                    ret[1] += 1
                else:
                    ret[0] += nums[0]
                    ret[1] += nums[1]
        return ret

#--- 출력 파트 ---#
nums = recursion(N, 0, 0)
if nums[1] == 0:
    print(1)
    print(0)
elif nums[0] == 0:
    print(0)
    print(1)
else:
    print(nums[0])
    print(nums[1])