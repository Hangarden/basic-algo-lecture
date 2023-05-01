import sys

#--- 입력 파트 ---#
N = int(input())
heights = []
for _ in range(N):
    heights.append(int(sys.stdin.readline().rstrip()))

#--- 로직 파트 ---#
stack = []
counts = [0] * N
ans = 0
for i in range(len(heights)-1, -1, -1):
    height = heights[i]
    while stack:
        if heights[stack[-1]] < height:
            popped_index = stack.pop()
            counts[i] += counts[popped_index] + 1
            ans += counts[popped_index] + 1
        else:
            break
    stack.append(i)

#--- 출력 파트 ---#
print(ans)