import sys

#--- 입력 파트 ---#
N = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

#--- 로직 파트 ---#
stack = []
ans = [0] * N
for i in range(N):
    num = nums[i]
    while stack:
        if nums[stack[-1]] <= num:
            stack.pop()
        else:
            ans[i] = stack[-1] + 1
            break
    stack.append(i)

#--- 출력 파트 ---#
for i in ans:
    print(i, end=" ")