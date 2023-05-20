# 순열
#--- 입력 파트 ---#
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

#--- 로직 파트 ---#
visited = [False] * N
def permu(items):
    if len(items) == M:
        for item in items:
            print(item, end=" ")
        print()
    else:
        for i in range(len(nums)):
            if visited[i] == False:
                num = nums[i]
                visited[i] = True
                permu(items + [num])
                visited[i] = False

#--- 출력 파트 ---#
permu([])