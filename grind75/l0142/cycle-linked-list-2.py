from common.list import ListNode
from typing import Optional


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or head.next:
        return 
    
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            rst = head
            while rst != slow:
                rst = rst.next
                slow = slow.next
            return rst
