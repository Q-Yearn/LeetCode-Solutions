class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tmp = {}
        for num in nums:
            if num not in tmp:
                tmp[num] = 1
            else:
                tmp[num] += 1
        tmp1 = list(tmp.items())
        tmp1.sort(key=lambda x:x[1], reverse=True)
        return [tmp1[i][0] for i in range(0, k)]
