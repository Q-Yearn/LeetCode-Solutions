# 效率低   超时了
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.LRU = {}
        self.capacity = capacity
        self.life = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i in self.life:
            self.life[i] += 1
        if key in self.LRU:
            self.life[key] = 0
            return self.LRU[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for i in self.life:
            self.life[i] += 1
        if key in self.LRU:
            self.LRU[key] = value
            self.life[key] = 0
        else:
            if len(self.LRU) < self.capacity:
                self.LRU[key] = value
                self.life[key] = 0
            else:
                max_key = max(self.life, key=self.life.get)
                self.LRU.pop(max_key)
                self.life.pop(max_key)
                self.LRU[key] = value
                self.life[key] = 0
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)