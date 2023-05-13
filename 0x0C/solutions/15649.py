# 순열
#--- 입력 파트 ---#
N, M = map(int, input().split())

#--- 로직 파트 ---#
visited = [False] * (N+1)
def permu(items):
    if len(items) == M:
        for item in items:
            print(item, end=" ")
        print()
    for num in range(1, N+1):
        if visited[num] == False:
            items.append(num)
            visited[num] = True
            permu(items)
            items.pop()
            visited[num] = False

#--- 출력 파트 ---#
permu([])