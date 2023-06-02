# 버블 소트
#--- 입력 파트 ---#
nums = []
N = int(input())
for _ in range(N):
    nums.append(int(input()))

#--- 로직 파트 ---#
for i in range(N-1):
    for j in range(N-1-i):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

#--- 출력 파트 ---#
for num in nums:
    print(num)