class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def print_list(head):
        rst = []
        while head:
            rst.append(head.val)
            head = head.next
        print(rst)
        return rst