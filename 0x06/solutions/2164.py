from collections import deque

#--- 입력 파트 ---#
N = int(input())
dq = deque([n for n in range(1, N+1)])

#--- 로직 파트 ---#
while len(dq) > 1:
    dq.popleft()
    dq.append((dq.popleft()))

#--- 출력 파트 ---#
print(dq.pop())