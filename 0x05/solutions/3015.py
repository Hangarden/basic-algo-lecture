# 스택을 활용한 풀이
import sys

#--- 입력 파트 ---#
N = int(input())
heights = []
for _ in range(N):
    heights.append(int(sys.stdin.readline().rstrip()))

#--- 로직 파트 ---#
stack = []
counts = [[0, 0] for _ in range(N)]  # counts[i][0]: i번째 사람이 만날 수 있는 사람의 숫자, counts[i][1]: i번째 사람과 height가 같은 사람들의 수
for i in range(N):
    # print(counts)
    height = heights[i]
    while stack and heights[stack[-1]] <= height:  # 나의 height보다 같거나 같으면 pop할 것이다
        if height == heights[stack[-1]]:  # 만일 나와 height가 같다면,
            counts[i][1] += (1 + counts[stack[-1]][1])  # '나와 height가 같은 사람들의 수'를 업데이트 해준다
        popped = stack.pop()
        counts[i][0] += 1 + counts[popped][1]
    if stack:  # 나보다 height가 큰 사람과 부딪힌 경우
        counts[i][0] += 1  # 그 사람과 마주보는 것이므로 ++1 한다
    stack.append(i)  # 자기 자신은 무조건 스택에 추가
# print(counts)

#--- 출력 파트 ---#
ans = 0
for i in range(N):
    ans += counts[i][0]
print(ans)


"""
4
4
2
2
5
정답: 6

4
1
5
1
1
정답: 4

4
1
1
1
5
정답: 6

4
1
1
1
1
정답: 6

5
1
5
1
1
6
정답: 7
"""