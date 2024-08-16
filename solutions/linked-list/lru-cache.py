class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()  # LRU
        self.tail = ListNode()  # MRU

        self.head.prev = self.tail
        self.tail.next = self.head

    def _remove(self, node: ListNode):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node: ListNode):
        prev, nxt = self.head.prev, self.head
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.tail.next
            self._remove(lru)
            del self.cache[lru.key]


lru_cache = LRUCache(2)

lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))
lru_cache.put(3, 3)
print(lru_cache.get(2))
lru_cache.put(4, 4)
print(lru_cache.get(1))
print(lru_cache.get(3))
print(lru_cache.get(4))
