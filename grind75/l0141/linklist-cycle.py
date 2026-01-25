
from typing import Optional

from common.list import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False
    
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True
    
    return False