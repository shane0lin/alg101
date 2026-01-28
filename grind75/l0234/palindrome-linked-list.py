from typing import Optional
from common.list import ListNode


def isPalindrome(head: Optional[ListNode]) -> bool:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]
