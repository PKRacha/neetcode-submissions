"""
1. Clarity questions
   - What should happen if the cache is at capacity and we add a new key? The least recently used item must be evicted.
   - Do 'get' and 'put' operations both count as usage? Yes, both move a key to the 'most recently used' position.
   - Is the capacity fixed at initialization? Yes.

2. Corner cases to consider
   - Capacity of 1.
   - Accessing a key that doesn't exist ('get' returns -1).
   - 'put' updating an existing key's value.
   - 'put' adding a key when the cache is already at full capacity.

3. Brute force Approach
   - Store items in a standard list.
   - 'get': Search list, remove item, append to end, return value.
   - 'put': If key exists, remove and update; if new, append. If over capacity, remove index 0.
   - Time: O(n) for both operations due to list traversal and shifting elements.

4. Best Approach
   - Combine a Hash Map (dictionary) with a Doubly Linked List.
   - Hash Map provides O(1) access to nodes.
   - Doubly Linked List provides O(1) removal and insertion at ends.
   - Use dummy 'left' (LRU) and 'right' (MRU) nodes to simplify edge cases.

5. Logic walk through
   Capacity = 2, Operations: put(1,1), put(2,2), get(1), put(3,3)
   [Initial: LRU(left) <-> MRU(right)]
   [Action 1: put(1,1) -> left <-> 1 <-> right]
   [Action 2: put(2,2) -> left <-> 1 <-> 2 <-> right]
   [Action 3: get(1) -> move 1 to MRU -> left <-> 2 <-> 1 <-> right]
   [Action 4: put(3,3) -> 2 is LRU, remove it -> left <-> 1 <-> 3 <-> right]
   [Final result/Update: Cache holds keys 1 and 3]

6. Time and space complexity
   - Time: O(1) for both get and put.
   - Space: O(capacity) to store the nodes in the map and list.

7. Code
"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]