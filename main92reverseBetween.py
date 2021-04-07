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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        i = 1
        front = None
        revershead = head
        while left != i:
            front = revershead
            revershead = revershead.next
            i += 1
        back = revershead
        while right != i:
            back = back.next
            i += 1
        last = back.next
        back.next = None

        cur = revershead
        while cur.next:
            next = cur.next
            cur.next = last
            last = cur
            cur = next
        cur.next = last
        if front:
            front.next = cur
            return head
        else:
            return cur


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    left = 1
    right = 4
    head = ListNode.build(nums)
    solution.reverseBetween(head, left, right)
