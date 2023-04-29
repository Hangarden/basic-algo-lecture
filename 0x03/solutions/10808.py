#--- 입력 파트 ---#
char_counts = [0] * 26

#--- 로직 파트 ---#
s = input()
for c in s:
    char_counts[ord(c)-97] += 1

#--- 출력 파트 ---#
for char_count in char_counts:
    print(char_count, end=' ')