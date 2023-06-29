#--- 입력 파트 ---#
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

#--- 로직 파트 ---#
dic = dict()
def combi(start, items):
    if len(items) == M:
        key = ''.join(str(items))
        if key not in dic:
            for item in items:
                print(item, end=" ")
            print()
            dic[key] = True
    else:
        for i in range(start, N):
            combi(i+1, items + [nums[i]])

#--- 출력 파트 ---#
combi(0, [])