#--- 입력 파트 ---#
s = input()

#--- 로직 파트 ---#
stack = []
count = 0  # '('의 갯수
ans = 0
for c in s:
    if c == ')':
        count -= 1
        if stack and stack[-1] == '(':  # 레이저를 발사한 경우
            ans += count
        else:  # 막대가 끝난경우
            ans += 1  # 막대가 잘라내진 끝부분 1개
    else:
        count += 1
    stack.append(c)

#--- 출력 파트 ---#
print(ans)