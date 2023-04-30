# 스택을 활용한 풀이
import sys

#--- 입력 파트 ---#
T = int(input())

for _ in range(T):
    s = sys.stdin.readline().rstrip()

    #--- 로직 파트 ---#
    stack_left = []
    stack_right = []
    for c in s:
        if c == '<':
            if stack_left: stack_right.append(stack_left.pop())
        elif c == '>':
            if stack_right: stack_left.append(stack_right.pop())
        elif c == '-':
            if stack_left: stack_left.pop()
        else:
            stack_left.append(c)

    #--- 출력 파트 ---#
    for c in stack_left:
        print(c, end="")
    while stack_right:
        print(stack_right.pop(), end="")
    print()