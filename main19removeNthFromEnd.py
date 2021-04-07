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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        while n > 0:
            n -= 1
            fast = fast.next
        slow = head
        if not fast:
            return slow.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    n = 2
    head = ListNode.build(nums)
    solution.removeNthFromEnd(head, n)