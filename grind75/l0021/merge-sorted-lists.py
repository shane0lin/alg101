
from typing import Optional

from common.list import ListNode

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return

    dummy = head = ListNode(0)

    while list1 and list2:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        
        head = head.next

    if list1:
        head.next = list1
    
    if list2:
        head.next = list2
    
    return dummy.next
    
