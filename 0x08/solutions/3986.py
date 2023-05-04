#--- 입력 파트 ---#
N = int(input())

#--- 로직 파트 ---#
ans = 0
for _ in range(N):
    s = input()
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        ans += 1

#--- 출력 파트 ---#
print(ans)