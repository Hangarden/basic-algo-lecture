# 중복 허용 조합
#--- 입력 파트 ---#
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

#--- 로직 파트 ---#
def combi(start, items):
    if len(items) >= M:
        for item in items:
            print(item, end=" ")
        print()
    else:
        for i in range(start, N):
            combi(i, items + [nums[i]])

#--- 출력 파트 ---#
combi(0, [])