import sys
from collections import deque

T = int(input())

for _ in range(T):
    #--- 입력 파트 ---#
    orders = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    s = s[1:len(s) - 1]  # O(n)
    if s == "":
        nums_dq = deque([])
    else:
        nums_dq = deque(list(map(int, s.split(","))))

    #--- 로직 파트 ---#
    is_errored = False
    is_reversed = False
    for order in orders:
        if order == 'R':
            is_reversed = not is_reversed  # 실제로 뒤집게 되면 시간 복잡도가 O(n^2)이 된다. 그러니 뒤집은 것 처럼 처리한다
        elif order == 'D':
            if is_reversed:
                if nums_dq:
                    nums_dq.pop()  # 뒤집혀졌다 가정하고 맨 뒤에 있는 숫자를 pop한다
                else:
                    is_errored = True  # 에러 마킹하고 break 한다
                    break
            else:
                if nums_dq:
                    nums_dq.popleft()  # 뒤집혀지지 않으면 문제에서 요구하는대로 맨 앞의 숫자를 popleft한다
                else:
                    is_errored = True  # 에러 마킹하고 break 한다
                    break

    #--- 출력 파트 ---#
    if is_errored:
        print("error")
    else:
        print("[", end="")
        if is_reversed and nums_dq:
            if nums_dq:
                print(nums_dq.pop(), end="")
            while nums_dq:
                print(f',{nums_dq.pop()}', end="")
        else:
            if nums_dq:
                print(nums_dq.popleft(), end="")
            while nums_dq:
                print(f',{nums_dq.popleft()}', end="")
        print("]")
