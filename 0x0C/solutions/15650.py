# 조합
#--- 입력 파트 ---#
N, M = map(int, input().split())

#--- 로직 파트 ---#
def combi(items, start):
    if len(items) == M:
        for item in items:
            print(item, end=" ")
        print()
    else:
        for i in range(start, N):
            item = i + 1
            combi(items + [item], i+1)

#--- 출력 파트 ---#
combi([], 0)