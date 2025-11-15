# 超时
class MedianFinder(object):

    def __init__(self):
        self.stream = []
        self.length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        i = 0
        while i < self.length:
            if num < self.stream[i]:
                break
            i += 1
        self.stream.insert(i, num)
        self.length += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.length % 2 == 1:
            return self.stream[self.length // 2]
        else:
            return (self.stream[self.length // 2 - 1] + self.stream[self.length // 2]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()