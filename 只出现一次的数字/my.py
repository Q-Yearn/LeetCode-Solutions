class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = {}
        for i, num in enumerate(nums):
            if num not in tmp:
                tmp[num] = i
            else:
                tmp.pop(num)
        for num in tmp:
            return num

# 不需要下标，使用集合即可
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = set()
        for num in nums:
            if num not in tmp:
                tmp.add(num)
            else:
                tmp.remove(num)
        # 集合的pop随机删除一个元素  字典的pop必须传入key然会value
        return tmp.pop()
