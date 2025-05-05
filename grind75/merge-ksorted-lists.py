# 23    Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Definition for singly-linked list.
from typing import List
from heapq import heappop, heappush, heapify

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists:
        return None
    amount = len(lists)
    dummy = ListNode(0)
    cur = dummy
    heap = []
    for i in range(amount):
        if lists[i]:
            heappush(heap, (lists[i].val, i, lists[i]))
    while heap:
        val, index, node = heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heappush(heap, (node.next.val, index, node.next))
    return dummy.next



    