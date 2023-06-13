import sys
from collections import deque

#--- 입력 파트 ---#
N, M = map(int, input().split())
matrix = [[0 for col in range(M)] for row in range(N)]
visited = [[[False for depth in range(2)] for col in range(M)] for row in range(N)]  # (핵심) 노드는 두 번 방문 가능하다: 벽을 부수고 방문하거나 벽을 부수지 않고 방문하는 것
for i in range(N):
    nums = sys.stdin.readline().rstrip()
    for j in range(M):
        matrix[i][j] = int(nums[j])

#--- 로직 파트 ---#
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
dq = deque()
dq.append([0, 0, False])  # row, col, 벽부쉈는지 여부
visited[0][0][0] = True  # 시작 칸은 무조건 전부 방문처리 한다
visited[0][0][1] = True
count = 0
ans = -1
while dq:
    temp_dq = deque()
    count += 1
    while dq:
        polled = dq.popleft()
        r = polled[0]
        c = polled[1]
        is_broken = polled[2]
        if r == N-1 and c == M-1:  # 끝에 도달한 경우
            ans = count  # 정답 저장하고 루프문 빠져나온다
            temp_dq = deque()
            break
        for d in range(4):
            dr = r + drs[d]
            dc = c + dcs[d]
            if 0<=dr<N and 0<=dc<M:
                if is_broken:  # 만일 벽을 하나 깬 것이라면
                    if matrix[dr][dc] == 0 and visited[dr][dc][1] == False:  # 비어있는 칸인 동시에 && 벽을 부수고 방문할 수 있을 때에만 덱에 노드를 추가한다
                        temp_dq.append([dr, dc, True])
                        visited[dr][dc][1] = True
                else:  # 만일 벽을 하나도 깨지 않았다면
                    if matrix[dr][dc] == 0 and visited[dr][dc][0] == False:  # 비어있는 칸은 일반적인 BFS 때처럼 방문처리여부 판단하고 덱에 추가한다
                        temp_dq.append([dr, dc, False])
                        visited[dr][dc][0] = True
                    elif matrix[dr][dc] == 1 and visited[dr][dc][1] == False:  # 벽인 동시에 && 아직 벽을 부수고 방문한 적이 없는 노드라면
                        temp_dq.append([dr, dc, True])  # 덱에 추가하고
                        visited[dr][dc][1] = True  # 벽을 부수고 방문한 것으로 처리한다
    dq = temp_dq

#--- 출력 파트 ---#
print(ans)

"""
가장 유의해야 하는 케이스는 아래와 같다
4 7
0110000
0110110
0110110
0000110
정답: 16

1 1
0
정답: 1
"""