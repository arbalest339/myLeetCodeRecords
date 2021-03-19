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
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        last = head
        cur = head.next
        while cur:
            next = cur.next
            cur.next = last
            last = cur
            cur = next

        head.next = None

        return last


if __name__ == "__main__":
    solution = Solution()
    listVal = [1, 2, 3, 4, 5]
    head = ListNode.genList(listVal)
    print(solution.reverseList(head))
