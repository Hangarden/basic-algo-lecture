import sys
from collections import deque

#--- 입력 파트 ---#
N = int(input())

#--- 로직 파트 ---#
dq = deque()
for _ in range(N):
    order = list(map(str, sys.stdin.readline().rstrip().split()))
    if order[0] == 'push':
        dq.append(order[1])
    elif order[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif order[0] == 'size':
        print(len(dq))
    elif order[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif order[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])