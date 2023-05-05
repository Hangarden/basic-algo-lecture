T = int(input())

for _ in range(T):
    # --- 입력 파트 ---#
    s = input()

    # --- 로직 파트 ---#
    stack = []
    for c in s:
        if c == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(c)

    # --- 출력 파트 ---#
    if stack:
        print("NO")
    else:
        print("YES")