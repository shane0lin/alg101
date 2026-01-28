from typing import Optional

from common.list import ListNode


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    prev, tail = dummy, head
    i = 0
    while tail and i < n:
        tail = tail.next
        i += 1
    
    while tail:
        prev = prev.next
        head = head.next
        tail = tail.next
        
    prev.next = head.next
    head.next = None

    return dummy.next