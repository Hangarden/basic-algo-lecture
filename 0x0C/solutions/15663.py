#--- 입력 파트 ---#
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

#--- 로직 파트 ---#
dic = dict()  # 중복 수열을 체크하기 위한 딕셔너리
visited = [False] * N
def permu(items):
    if len(items) >= M:
        k = str(items)
        if k not in dic:
            for item in items:
                print(item, end=" ")
            print()
            dic[k] = True
    else:
        for i in range(N):
            num = nums[i]
            if visited[i] == False:
                visited[i] = True
                permu(items + [num])
                visited[i] = False

#--- 출력 파트 ---#
permu([])