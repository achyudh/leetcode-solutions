class CacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prevPtr = None
        self.nextPtr = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def popTail(self):
        removed_node = self.tail
        if self.head == self.tail:
            self.head = None
        self.tail = self.tail.prevPtr
            self.tail.nextPtr = None
        return removed_node

    
    def pushHead(self, node):
        node.prevPtr = None
        node.nextPtr = self.head
        if self.head:
            self.head.prevPtr = node
        self.head = node
        if not self.tail:
            self.tail = node

    def remove(self, node):
        if node.nextPtr:
            node.nextPtr.prevPtr = node.prevPtr
            if node.prevPtr:
                node.prevPtr.nextPtr = node.nextPtr
            else:
                self.head = node.nextPtr
        else:   
            self.popTail()


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.deque = Deque()
        self.nodeMap = dict()

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.deque.remove(node)
            self.deque.pushHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.deque.remove(node)
            node.value = value
        else:
            node = CacheNode(key, value)
            if len(self.nodeMap) == self.capacity:
                removed_node = self.deque.popTail()
                self.nodeMap.pop(removed_node.key)
            self.nodeMap[key] = node  
        self.deque.pushHead(node)

# cache = LRUCache(10)
# actions = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# values = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

# for action, value in zip(actions, values):
#     print(action, value)
#     if action == "put":
#         cache.put(value[0], value[1])
#     elif action == "get":
#         cache.get(value[0])
