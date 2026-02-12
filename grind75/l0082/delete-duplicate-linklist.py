
from typing import Optional

from common.list import ListNode


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if not cur.next:
                break

            if cur.val != cur.next.val:
                prev = cur
                cur = cur.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
                cur.next = None
                cur = prev.next
        return dummy.next