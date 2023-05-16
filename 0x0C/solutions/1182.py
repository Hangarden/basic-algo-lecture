#---입력 파트---#
N, S = map(int, input().split())
nums = list(map(int, input().split()))

#---로직 파트---#
def subset(summation, start):
    if start == N:
        if summation == S:
            return 1
        else:
            return 0
    else:
        ret = 0
        ret += subset(summation + nums[start], start+1)
        ret += subset(summation, start+1)
        return ret

#---출력 파트---#
count = subset(0, 0)
if S == 0:  # 목표합이 0인경우 공집합을 제외해야 한다
    print(count - 1)
else:
    print(count)