class DoubleList:
    def __init__(self, val, prev=None, post=None):
        self.val = val
        self.prev = prev
        self.post = post


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        head = DoubleList("#")
        tail = DoubleList("#")
        head.post = "tail"
        tail.prev = "head"
        self.map["head"] = head
        self.map["tail"] = tail

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            prev = self.map[key].prev
            post = self.map[key].post
            self.map[prev].post = post
            self.map[post].prev = prev
            self.map[key].prev = "head"
            self.map[key].post = self.map["head"].post
            post = self.map["head"].post
            self.map[post].prev = key
            self.map["head"].post = key
            return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.map and len(self.map)-2 < self.capacity:
            node = DoubleList(value)
            node.prev = "head"
            node.post = self.map["head"].post
            post = self.map["head"].post
            self.map[post].prev = key
            self.map["head"].post = key
            self.map[key] = node
        elif key not in self.map:
            node = DoubleList(value)
            node.prev = "head"
            node.post = self.map["head"].post
            post = self.map["head"].post
            self.map[post].prev = key
            self.map["head"].post = key
            self.map[key] = node
            last = self.map["tail"].prev
            self.map["tail"].prev = self.map[last].prev
            self.map[self.map["tail"].prev].post = "tail"
            self.map.pop(last)
        else:
            self.map[key].val = value
            prev = self.map[key].prev
            post = self.map[key].post
            self.map[prev].post = post
            self.map[post].prev = prev
            self.map[key].prev = "head"
            self.map[key].post = self.map["head"].post
            post = self.map["head"].post
            self.map[post].prev = key
            self.map["head"].post = key


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
