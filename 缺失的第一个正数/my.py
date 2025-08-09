class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        tmp = set()
        for num in nums:
            tmp.add(num)
        i = 1
        while i in tmp:
            i += 1
        return i
        