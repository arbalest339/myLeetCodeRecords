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
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        if head.next:
            fast = head.next
        else:
            return slow
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            if fast.next:
                fast = fast.next
            else:
                return slow
        slow = slow.next
        return slow

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5,6]
    head = ListNode.build(nums)
    solution.middleNode(head)