class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        fast = head
        slow = head
        while fast.next and slow.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow= slow.next
            if fast == slow:
                break
            
        if fast.next and slow.next:
            res = head
            while res != slow:
                res= res.next
                slow = slow.next
            return res
        return -1

if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2
    solution.detectCycle(l1)