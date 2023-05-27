#--- 입력 파트 ---#
import math

N, K = map(int, input().split())
students = [[0 for year in range(7)] for gender in range(2)]
for _ in range(N):
    S, Y = map(int, input().split())  # S: 성별, Y: 학년
    students[S][Y] += 1

#--- 로직 파트 ---#
ans = 0
for student in students:
    for num in student:
        ans += math.ceil(num/K)

#--- 출력 파트 ---#
print(ans)