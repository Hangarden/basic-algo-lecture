#--- 입력 파트 ---#
string_A = input()
string_B = input()

#--- 로직 파트 ---#
char_countA = [0] * 26
char_countB = [0] * 26
for charA in string_A:
    char_countA[ord(charA)-97] += 1
for charB in string_B:
    char_countB[ord(charB)-97] += 1

ans = 0
for i in range(26):
    ans += abs(char_countA[i] - char_countB[i])

#--- 출력 파트 ---#
print(ans)