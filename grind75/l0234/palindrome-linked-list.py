from typing import Optional
from common.list import ListNode


def isPalindrome(head: Optional[ListNode]) -> bool:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]


a = ListNode(1)
b = ListNode(2)
c = ListNode(5)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e

ListNode.print_list(a)
print(isPalindrome(a))
print(isPalindrome(b))