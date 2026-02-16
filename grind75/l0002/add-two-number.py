from typing import Optional
from common.list import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    q1 = []
    head = l1
    while head:
        q1.append(head.val)
        head = head.next
    
    q2 = []
    head = l2
    while head:
        q2.append(head.val)
        head = head.next
    
    q3 = []
    carryover = 0
    while q1 and q2:
        a = q1.pop()
        b = q2.pop()
        sum_ = a + b + carryover
        q3.append(sum_ % 10)
        carryover = sum_ // 10
    
    while q1:
        a = q1.pop()
        sum_ = a + carryover
        q3.append(sum_ % 10)
        carryover = sum_ // 10
    
    while q2:
        a = q2.pop()
        sum_ = a + carryover
        q3.append(sum_ % 10)
        carryover = sum_ // 10
    
    if carryover:
        q3.append(carryover)
    
    q3 = q3[::-1]
    dummy = ListNode()
    tail = dummy
    while q3:
        a = q3.pop()
        node = ListNode(a)
        tail.next = node
        tail = node
    return dummy.next