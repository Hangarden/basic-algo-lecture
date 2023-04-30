# --- 입력 파트 ---#
N, K = map(int, input().split())

# --- 로직 파트 ---#
nums = [num for num in range(1, N+1)]
cur = 0  # 제거될 숫자를 가리키는 커서
ans = []
while nums:
    cur += (K-1)
    cur = cur % len(nums)
    ans.append(nums.pop(cur))

# --- 출력 파트 ---#
print("<", end="")
last_num = ans.pop()
for num in ans:
    print(num, end=", ")
print(f'{last_num}>')