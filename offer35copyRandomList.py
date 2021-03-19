class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    @staticmethod
    def genNodeList(nodes):
        listnodes = []
        for node in nodes:
            newnode = Node(node[0])
            listnodes.append(newnode)
        for i, node in enumerate(nodes):
            if node[1] != None:
                listnodes[i].random = listnodes[node[1]]
            if i < len(listnodes)-1:
                listnodes[i].next = listnodes[i+1]

        return listnodes[0]


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        while cur:
            new_node = Node(cur.val, None, None)   # 克隆新结点
            new_node.next = cur.next
            cur.next = new_node   # 克隆新结点在cur 后面
            cur = new_node.next   # 移动到下一个要克隆的点
        cur = head

        while cur:  # 链接random
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur_old_list = head  # 将两个链表分开
        cur_new_list = head.next
        new_head = head.next
        while cur_old_list:
            cur_old_list.next = cur_old_list.next.next
            cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
            cur_old_list = cur_old_list.next
            cur_new_list = cur_new_list.next
        return new_head


if __name__ == "__main__":
    solution = Solution()
    head = Node.genNodeList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    solution.copyRandomList(head)
