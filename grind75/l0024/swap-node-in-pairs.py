from typing import Optional
from common.list import ListNode


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    

    p, q = head, head.next
    dummy = ListNode()
    pre = dummy


    while p and q:
        pre.next = q
        pre = p
        p.next = q.next
        q.next = p
        p = p.next
        if p:
            q = p.next
        
    dummy.print_list(dummy.next)
    return dummy.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

a.print_list(a)
swapPairs(head=a)