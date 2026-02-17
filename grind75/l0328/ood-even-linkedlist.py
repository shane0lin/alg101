from typing import Optional
from common.list import ListNode


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next or not head.next.next:
        return head
    
    odd = head
    even = even_head = head.next 
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    
    odd.next = even_head

    return head

