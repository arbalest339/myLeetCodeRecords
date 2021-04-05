class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def build(lst):
        if not lst:
            return
        res = ListNode(lst[0])
        last = res
        for i in range(1, len(lst)):
            cur = ListNode(lst[i])
            last.next = cur
            last = cur
        return res

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = l1.val+l2.val
        forward = first // 10
        first = first % 10
        res = ListNode(first)
        last = res
        while l1.next and l2.next:
            l1= l1.next
            l2=l2.next
            cur = l1.val+l2.val + forward
            forward = cur // 10
            cur = cur % 10
            cur = ListNode(cur)
            last.next = cur
            last = cur
        
        while l1.next:
            l1= l1.next
            cur = l1.val + forward
            forward = cur // 10
            cur = cur % 10
            cur = ListNode(cur)
            last.next = cur
            last = cur
        
        while l2.next:
            l2= l2.next
            cur = l2.val + forward
            forward = cur // 10
            cur = cur % 10
            cur = ListNode(cur)
            last.next = cur
            last = cur

        if forward == 1:
            cur = ListNode(1)
            last.next = cur
        return res


if __name__ == "__main__":
    lst1 = [2,4,3]
    l1 = ListNode.build(lst1)
    lst2 = [5,6,4]
    l2 = ListNode.build(lst2)
    solu = Solution()
    solu.addTwoNumbers(l1, l2)