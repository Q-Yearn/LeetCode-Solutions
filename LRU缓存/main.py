# 用自带的库实现  python2  and python3
class LRUCache(collections.OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # python3写法
        # super().__init__()
        super(LRUCache, self).__init__()
        self.capacity = capacity

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1
        value = self.pop(key)
        self[key] = value
        # python3才有
        # 上面两行等同于这个
        # self.move_to_end(key)
        return self[key]

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:
            self.pop(key)
        self[key] = value
        if len(self) > self.capacity:
            # python3 写法
            # self.popitem(last=False)
            first_key = next(self.iterkeys())
            self.pop(first_key)
        

# 自行实现双向链表  和 使用哈希表  模拟
class DlinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.nex = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.nex = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            node = DlinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.pre = self.head
        node.nex = self.head.nex
        self.head.nex.pre = node
        self.head.nex = node
    
    def moveToHead(self, node):
        node.nex.pre = node.pre
        node.pre.nex = node.nex
        self.addToHead(node)
    
    def removeTail(self):
        node = self.tail.pre
        node.nex.pre = node.pre
        node.pre.nex = node.nex
        return node

        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)