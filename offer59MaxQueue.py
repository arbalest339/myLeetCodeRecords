class DoubleList:
    def __init__(self, val, prev=None, post=None):
        self.val = val
        self.prev = prev
        self.post = post

# class MaxQueue:

#     def __init__(self):
#         import collections
#         self.queue = collections.deque()
#         self.max = DoubleList(None)


#     def max_value(self) -> int:
#         if not self.max.post:
#             return -1
#         return self.max.post.val


#     def push_back(self, value: int) -> None:
#         node = DoubleList(value)
#         self.queue.append(node)
#         if not self.max.post:
#             self.max.post = node
#             node.prev = self.max
#             return
#         cur = self.max.post
#         while cur.post and cur.val > node.val:
#             cur = cur.post
#         if cur.val > node.val:
#             cur.post = node
#             node.prev = cur
#         else:
#             node.post = cur
#             node.prev = cur.prev
#             cur.prev.post = node
#             cur.prev = node

#     def pop_front(self) -> int:
#         if not self.queue:
#             return -1
#         node = self.queue.popleft()
#         prev = node.prev
#         post = node.post
#         prev.post = post
#         if post:
#             post.prev = prev
#         return node.val

class MaxQueue:

    def __init__(self):
        import queue
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:    # 如果后来的大于前面的，那前面的必定先出去，故已经不可能成为最大值了
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

if __name__ == "__main__":
    queue = MaxQueue()
    queue.push_back(1)
    queue.push_back(2)
    queue.max_value()
    queue.pop_front()
    queue.max_value()
    queue.pop_front()
    queue.max_value()