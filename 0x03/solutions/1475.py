num_counts = [0] * 10  # 숫자를 사용한 횟수를 저장한다

#--- 입력 파트 ---#
num_string = input()

#--- 로직 파트 ---#
for num_char in num_string:
    num = int(num_char)
    # 6과 9중에서 더 적게 사용한 숫자를 선택하여 하나 더 사용한다
    if num == 6 or num == 9:
        if num_counts[6] <= num_counts[9]:
            num_counts[6] += 1
        else:
            num_counts[9] += 1
    else:
        num_counts[num] += 1

#--- 출력 파트 ---#
ans = 0
for num_count in num_counts:
    ans = max(ans, num_count)
print(ans)