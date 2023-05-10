"""
  1구역  |  2구역
-------------------
  3구역  |  4구역
"""

#--- 입력 파트 ---#
N, R, C = map(int, input().split())

#---로직 파트 ---#
def recursion(size, start_num, start_row, start_col):
    if size == 1:
        return start_num
    if R < start_row + size // 2:
        if C < start_col + size // 2:  # 1구역
            num = start_num
            return recursion(size // 2, num, start_row, start_col)
        else:  # 2구역
            num = start_num + (size // 2) * (size // 2)
            return recursion(size // 2, num, start_row, start_col + size//2)
    else:
        if C < start_col + size // 2:  # 3구역
            num = start_num + ((size // 2) * (size // 2)) * 2
            return recursion(size // 2, num, start_row + size//2, start_col)
        else:  # 4구역
            num = start_num + ((size // 2) * (size // 2)) * 3
            return recursion(size // 2, num, start_row + size//2, start_col + size//2)

#---출력 파트 ---#
print(recursion(2**N, 0, 0, 0))