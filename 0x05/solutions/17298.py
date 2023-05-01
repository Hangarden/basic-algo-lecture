import sys

#--- 입력 파트 ---#
N = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

#--- 로직 파트 ---#
ans = [-1] * N
stack = []
for i in range(len(nums)):
    num = nums[i]
    while stack and nums[stack[-1]] < num:
        ans[stack.pop()] = num
    stack.append(i)

#--- 출력 파트 ---#
for n in ans:
    print(n, end=" ")