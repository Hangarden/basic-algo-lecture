#--- 입력 파트 ---#
A, B, C = map(int, input().split())

#--- 로직 파트 ---#
def recursion(n):
    if n == 0:
        return 1
    elif n == 1:
        return A % C
    elif n % 2 == 0:
        ret = recursion(n//2)
        return ((ret % C) * (ret % C)) % C
    else:
        ret = recursion(n//2)
        return ((ret % C) * (ret % C) * (A % C)) % C

#--- 출력 파트 ---#
print(recursion(B))