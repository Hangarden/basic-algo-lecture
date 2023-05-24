#--- 입력 파트 ---#
N, M = map(int, input().split())
houses = []  # 집 좌표 저장
chickens = []  # 치킨집 좌표 저장
for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(N):
        if nums[j] == 1:
            houses.append([i, j])
        elif nums[j] == 2:
            chickens.append([i, j])

#--- 로직 파트 ---#
def combi(start, items):  # 치킨집 M개 만큼 고르기 위해 조합을 사용한다
    if len(items) == M:
        dist = 0  # dist: 문제에서 요구하는 치킨거리
        for house in houses:
            house_r = house[0]
            house_c = house[1]
            min_dist = 9999999  # 집마다 가장 가까운 치킨집 까지 거리를 찾아낸다
            for chicken in items:
                chicken_r = chicken[0]
                chicken_c = chicken[1]
                min_dist = min(min_dist, abs(chicken_r - house_r) + abs(chicken_c - house_c))
            dist += min_dist
        return dist
    else:
        min_dist = 99999  # dist: 문제에서 요구하는 치킨거리중 최소값
        for i in range(start, len(chickens)):
            item = chickens[i]
            min_dist = min(min_dist, combi(i+1, items + [item]))
        return min_dist

#--- 출력 파트 ---#
print(combi(0, []))