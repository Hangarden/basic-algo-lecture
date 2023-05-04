import sys

while True:
    #--- 입력 파트 ---#
    s = sys.stdin.readline().rstrip()
    if s == '.': break

    #--- 로직 파트 ---#
    stack = []
    ans = "yes"
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                continue
            else:
                ans = "no"
                break
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                continue
            else:
                ans = "no"
                break
    #--- 출력 파트 ---#
    if stack:
        print("no")
    else:
        print(ans)