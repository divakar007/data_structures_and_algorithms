class ListNode:
    def __init__(self, key,  val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.size = 0
        self.head = ListNode(-1, -1)  # dummy head
        self.tail = ListNode(-1, -1)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def get(self, key):
        node = self.map.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key, value):
        if self.cap == 0:      # edge case: cannot store anything
            return
        node = self.map.get(key)
        if node:
            node.val = value
            self._move_to_front(node)
            return
        if self.size == self.cap:
            self._evict()
        new_node = ListNode(key, value)
        self._insert_after_head(new_node)
        self.map[key] = new_node
        self.size += 1

    # --- helpers ---
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        node.prev = node.next = None

    def _insert_after_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node):
        # unlink first if already linked
        self._remove(node)
        self._insert_after_head(node)

    def _evict(self):
        # remove LRU node (node before tail) if present
        lru = self.tail.prev
        if lru is self.head:   # list empty guard
            return
        self._remove(lru)
        del self.map[lru.key]
        self.size -= 1
