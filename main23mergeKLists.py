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
    def mergeKLists(self, lists) -> ListNode:
        res = ListNode(None)
        cur = res
        deletes = []
        for i, lst in enumerate(lists):
            if not lst.val:
                deletes.append(i)
        for offset, i in enumerate(deletes):
            lists.pop(i-offset)
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        lists = sorted(lists, key=lambda x: x.val)

        while lists:
            cur.next = lists[0]
            cur = cur.next
            if not lists[0].next:
                lists.pop(0)
            else:
                lists[0] = lists[0].next
            if len(lists) == 1:
                cur.next = lists[0]
            else:
                for i in range(1, len(lists)):
                    if lists[i-1].val > lists[i].val:
                        lists[i-1], lists[i] = lists[i], lists[i-1]
                    else:
                        break

        return res.next


if __name__ == "__main__":
    solution = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [3, 4, 5], [2, 6]]
    # inputs = [ListNode.build(lst) for lst in lists]
    inputs = [ListNode(None),ListNode(None)]
    res = solution.mergeKLists(inputs)
    while res:
        print(res.val)
        res = res.next
