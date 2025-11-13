# 还得理解
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quicksearch(l, r, k):
            if l == r:
                return nums[k]
            num = nums[l]
            i, j = l-1, r+1
            while i < j :
                i += 1
                while nums[i] < num:
                    i += 1
                j -= 1
                while nums[j] > num:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if k <= j:
                return quicksearch(l, j, k)
            else:
                return quicksearch(j+1, r, k)
        
        return quicksearch(0, len(nums)-1, len(nums)-k)

# 大根堆
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = len(nums)
        self.buildmaxheap(nums, m)
        for i in range(m-1, m-k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            m -= 1
            self.maxheap(nums, 0, m)
        return nums[0]

    def buildmaxheap(self, nums, m):
        for i in range(m//2-1, -1, -1):
            self.maxheap(nums, i, m)
    
    def maxheap(self, nums, i, m):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < m and nums[left] > nums[largest]:
            largest = left
        if right < m and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.maxheap(nums, largest, m)