# ---입력 파트---#
N = int(input())

# ---로직 파트---#
visited_col = [False] * N
visited_slash = [False] * N * 2  # / 방향의 대각선 방문 여부 체크용 배열
visited_back_slash = [False] * N * 2  # \ 방행의 대각선 방문 여부 체크용 배열
def dfs(start_row: int):
    if start_row == N:  # 행이 범위 넘어갔다면 퀸을 N개 놓은 것이므로 count++을 위한 1을 리턴한다
        return 1
    else:
        count = 0
        for col in range(N):
            if visited_col[col] == False and visited_slash[start_row + col] == False and visited_back_slash[col - start_row + N-1] == False:  # 그전에 놓았던 퀸들과 겹치지 않는지 점검한다
                visited_col[col] = True
                visited_slash[col + start_row] = True
                visited_back_slash[col - start_row + N-1] = True

                count += dfs(start_row + 1)  # 다음 행에 대한 재귀호출

                # 방문 여부 원상복귀
                visited_col[col] = False
                visited_slash[col + start_row] = False
                visited_back_slash[col - start_row + N-1] = False
        return count

# ---출력 파트---#
print(dfs(0))