import sys

#--- 입력 파트 ---#
count = 0
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
x = int(input())

#--- 로직 파트 ---#
dic = dict()
for i in range(len(nums)):
    num = nums[i]
    dic[num] = i
for i in range(len(nums)):
    num = nums[i]
    if x <= num:
        continue
    else:
        target = x - num
        if target in dic:
            if i < dic[target]:
                count += 1

#--- 출력 파트 ---#
print(count)