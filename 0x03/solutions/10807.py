#--- 입력 파트 ---#
N = int(input())
nums = list(map(int, input().split()))
v= int(input())

#--- 로직 파트 ---#
dic = dict()
for num in nums:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

#--- 출력 파트 ---#
if v in dic:
    print(dic[v])
else:
    print(0)