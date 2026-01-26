from typing import Optional
from common.list import ListNode

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev
