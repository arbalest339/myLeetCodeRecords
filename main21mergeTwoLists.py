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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        res = head
        while l1 or l2:
            if l1 and (not l2 or l1.val<l2.val):
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        return head.next


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3, 7, 9, 11, 15]
    nums2 = [2, 6, 8, 12, 14]
    node1 = ListNode.build(nums1)
    node2 = ListNode.build(nums2)
    solution.mergeTwoLists(node1, node2)