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

def findCircleStart(head):
    if head and head.next:
        fast = head.next
    else:
        return None
    slow = head
    while fast.next and not fast is slow:
        fast = fast.next
        slow = slow.next
        if fast.next:
            fast = fast.next
        else:
            break
        if not fast.next:
            return None
        if fast is slow:
            return fast

def commonLengthNoCircle(l1, l2):
    cur1, cur2 = l1, l2
    secondLap1, secondLap2 = False, False
    while not cur1 is cur2:
        if cur1.next:
            cur1 = cur1.next
        elif not secondLap1:
            cur1 = l2
            secondLap1 = True
        else:
            return 0
        if cur2.next:
            cur2 = cur2.next
        elif not secondLap2:
            cur2 = l1
            secondLap2 = True
        else:
            return 0
    start = commonLengthNoCircle(l1, l2)
    l = 1
    while start.next:
        l += 1
    return l


def commonLength(l1, l2):
    o1 = findCircleStart(l1)
    o2 = findCircleStart(l2)
    l = 0
    if not o1 and not o2:   # 无环情况
        l = commonLengthNoCircle(l1, l2)
    elif o1 and o2:     # 有环情况
        cur = o1    # 无论如何环周长都是共同长度的一部分
        l = 1
        while cur.next is not o1:
            l += 1
        if o1 is o2:    # 进入环的位置不同，环周长即为共同长度
            o1.next = None
            l += commonLengthNoCircle(l1, l2)
    return l


if __name__ == "__main__":
    l1 = ListNode.build([1,2,3,4,5,6,7,8,9])
    cur = l1
    fifth = None
    while cur.next:
        if cur.val == 5:
            fifth = cur
        cur = cur.next
    cur.next = fifth
    l2 = ListNode.build([1,2])
    l2.next.next = fifth.next
    print(commonLength(l1, l2))