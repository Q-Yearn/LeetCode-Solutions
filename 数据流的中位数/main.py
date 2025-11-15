# 两个优先队列 python默认是小根堆
class MedianFinder(object):

    def __init__(self):
        self.quemin = []
        self.quemax = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.quemin or num <= -self.quemin[0]:
            heapq.heappush(self.quemin, -num)
            if len(self.quemin) == len(self.quemax) + 2:
                heapq.heappush(self.quemax, -heapq.heappop(self.quemin))
        else:
            heapq.heappush(self.quemax, num)
            if len(self.quemin) < len(self.quemax):
                heapq.heappush(self.quemin, -heapq.heappop(self.quemax))
  

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.quemax) == len(self.quemin):
            return (self.quemax[0] - self.quemin[0]) / 2.0
        else:
            return -self.quemin[0]


# 有序集合  那为什么还要这么写呢  自动排序了  直接输出不就好了
from sortedcontainers import SortedList
class MedianFinder(object):

    def __init__(self): 
        self.nums = SortedList()
        self.left = self.right = None
        self.left_value = self.right_value = None

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        n = len(self.nums)
        self.nums.add(num)
        
        if n == 0:
            self.left = self.right = 0
        else:
            if num < self.left_value:
                if n % 2 == 0:
                    self.left += 1
                else:
                    self.right += 1
            elif num >= self.right_value:
                if n % 2 == 0:
                    self.left += 1
                else:
                    self.right += 1
            elif self.left_value <= num < self.right_value:
                # 只可能是n%2为0时
                self.left += 1

        self.left_value = self.nums[self.left]
        self.right_value = self.nums[self.right]

    def findMedian(self):
        """
        :rtype: float
        """
        return (self.left_value + self.right_value) / 2.0


# 直接输出
from sortedcontainers import SortedList
class MedianFinder(object):

    def __init__(self): 
        self.nums = SortedList()

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.add(num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.nums) % 2 == 1:
            return self.nums[len(self.nums) // 2]
        else:
            return (self.nums[len(self.nums) // 2] + self.nums[len(self.nums) // 2 - 1]) / 2.0