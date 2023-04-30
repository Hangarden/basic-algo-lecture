import sys

#--- 입력 파트 ---#
N = int(input())
targets = []
for _ in range(N):
    targets.append(int(sys.stdin.readline().rstrip()))

#--- 로직 파트 ---#
stack = []
n = 1  # stack에 push될 숫자
cur = 0  # target을 지정하기 위한 인덱스
ans = []  # push, pop 정보를 담을 배열
popped_nums = []  # 스택 수열
while cur < N:
    target = targets[cur]  # 찾아야 할 수
    if not stack:  # 스택이 비어있으면 무조건 push 한다
        stack.append(n)
        ans.append('+')
        n += 1
        continue
    if stack and stack[-1] < target:
        stack.append(n)
        ans.append('+')
        n += 1
    elif stack and stack[-1] == target:
        popped_nums.append(stack.pop())
        ans.append('-')
        cur += 1
    else:
        break
        
#--- 출력 파트 ---#
if popped_nums == targets:
    for c in ans:
        print(c)
else:
    print("NO")