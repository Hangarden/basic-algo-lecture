# 스택을 활용한 풀이
import sys

#--- 입력 파트 ---#
S = sys.stdin.readline().rstrip()
M = int(input())

#--- 로직 파트 ---#
stack_left = []  # 커서를 기준으로 왼쪽에 있는 문자들을 담는 스택
stack_right = []  # 커서를 기준으로 오른쪽에 있는 문자들을 담는 스택
for c in S:
    stack_left.append(c)

for _ in range(M):
    order = list(sys.stdin.readline().split())
    if order[0] == 'L' and stack_left:
        stack_right.append(stack_left.pop())
    elif order[0] == 'D' and stack_right:
        stack_left.append(stack_right.pop())
    elif order[0] == 'B' and stack_left:
        stack_left.pop()
    elif order[0] == 'P':
        stack_left.append(order[1])

#--- 출력 파트 ---#
for c in stack_left:
    print(c, end="")
while stack_right:
    print(stack_right.pop(), end="")