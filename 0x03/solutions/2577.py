#--- 입력 파트 ---#
num_counts = [0] * 10
A = int(input())
B = int(input())
C = int(input())

#--- 로직 파트 ---#
for c in str(A*B*C):
    num = int(c)
    num_counts[num] += 1

#--- 출력 파트 ---#
for num_count in num_counts:
    print(num_count)