#--- 입력 파트 ---#
N = int(input())

#--- 로직 파트 ---#
# 하노이탑의 맨 위에서부터 움직일 생각을 하기보단 맨 아래의 원판을 움직이기 위해 위의 n-1개를 옮기는 방법을 재귀적으로 생각해야 한다
def one_two(n):
    if n == 1:
        print("1 2")
        return
    one_three(n-1)
    print("1 2")
    three_two(n-1)
def one_three(n):
    if n == 1:
        print("1 3")
    else:
        one_two(n-1)
        print("1 3")
        two_three(n-1)
def two_one(n):
    if n == 1:
        print("2 1")
    else:
        two_three(n-1)
        print("2 1")
        three_one(n-1)
def two_three(n):
    if n == 1:
        print("2 3")
    else:
        two_one(n-1)
        print("2 3")
        one_three(n-1)
def three_one(n):
    if n == 1:
        print("3 1")
    else:
        three_two(n-1)
        print("3 1")
        two_one(n-1)
def three_two(n):
    if n == 1:
        print("3 2")
    else:
        three_one(n-1)
        print("3 2")
        one_two(n-1)

#--- 출력 파트 ---#
print(2**N-1)
one_three(N)