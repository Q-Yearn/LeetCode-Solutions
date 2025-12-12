class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = set()
        for num in nums:
            if num not in tmp:
                tmp.add(num)
            else:
                return num
        