class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.
        """
        self.capacity = capacity
        self.cache = {}

        self.lru = ListNode()  # Least Recently Used (dummy head)
        self.mru = ListNode()  # Most Recently Used (dummy tail)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self, node: ListNode):
        """
        Remove a node from the doubly linked list.
        """
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: ListNode):
        """
        Insert a node right before the most recently used (MRU) node.
        """
        last_node = self.mru.prev
        last_node.next = node
        node.prev = last_node
        self.mru.prev = node

    def get(self, key: int) -> int:
        """
        Return the value of the node with the given key if present, 
        otherwise return -1.
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Add a new key-value pair to the cache or update the value of an existing key.
        """
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.lru.next
            self.remove(node)
            del self.cache[node.key]


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
