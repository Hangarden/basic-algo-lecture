import sys

#--- 입력 파트 ---#
K = int(input())

#--- 로직 파트 ---#
stack = []
summation = 0
for _ in range(K):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        summation -= stack.pop()
    else:
        summation += num
        stack.append(num)

#--- 출력 파트 ---#
print(summation)