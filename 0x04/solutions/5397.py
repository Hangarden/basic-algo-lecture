# Linked List로 풀이하였음
# Python3로 제출하면 시간초과가 발생함. pypy로 제출하면 통과됨

import sys

class ListNode:
    def __init__(self, val="", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

T = int(input())
for _ in range(T):
    # --- 입력 파트 ---#
    s = sys.stdin.readline().rstrip()

    # --- 로직 파트 ---#
    head = ListNode()
    cur = head
    for c in s:
        if c == "<":
            if cur == head:
                continue
            else:
                cur = cur.prev
        elif c == '>':
            if cur.next == None:
                continue
            else:
                cur = cur.next
        elif c == '-':
            if cur == head:
                continue
            else:
                temp = cur.prev
                temp.next = cur.next
                if cur.next:
                    cur.next.prev = temp
                cur.prev = None
                cur.next = None
                cur = temp
        else:
            temp = ListNode(val=c, prev=cur, next=cur.next)
            if cur.next:
                cur.next.prev = temp
            cur.next = temp
            cur = temp

    # --- 출력 파트 ---#
    while head:
        print(head.val, end="")
        head = head.next
    print()