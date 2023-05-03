from collections import deque

#--- 입력 파트 ---#
N, M = map(int, input().split())
nums = list(map(int, input().split()))

#--- 로직 파트 ---#
count = 0
dq = deque([n for n in range(1, N+1)])
for num in nums:
    pos = 0
    for i in range(len(dq)):
        if dq[i] == num:
            pos = i
            break
    if pos <= len(dq) // 2:
        for _ in range(pos):
            count += 1
            dq.append(dq.popleft())
    else:
        for _ in range(len(dq)-pos):
            count += 1
            dq.appendleft(dq.pop())
    dq.popleft()

#--- 출력 파트 ---#
print(count)