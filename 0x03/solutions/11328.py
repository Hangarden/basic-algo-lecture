T = int(input())

for _ in range(T):
    # --- 입력 파트 ---#
    strA, strB = map(str, input().split())

    # --- 로직 파트 ---#
    charA_counts = [0] * 26
    charB_counts = [0] * 26
    for charA in strA:
        charA_counts[ord(charA)-97] += 1
    for charB in strB:
        charB_counts[ord(charB)-97] += 1

    # --- 출력 파트 ---#
    if charA_counts == charB_counts:
        print("Possible")
    else:
        print("Impossible")
