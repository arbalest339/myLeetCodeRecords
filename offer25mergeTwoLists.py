class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    @staticmethod
    def genList(listVal):
        head = cur = ListNode(listVal[0])
        for val in listVal[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif not l1 and not l2:
            return None
        
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next

        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        
        if not l1:
            cur.next = l2
        elif not l2:
            cur.next = l1

        return head


if __name__ == "__main__":
    solution = Solution()
    listVal = [1,2,4]
    head1 = ListNode.genList(listVal)
    listVal = [1,3,4]
    head2 = ListNode.genList(listVal)
    print(solution.mergeTwoLists(head1,head2))