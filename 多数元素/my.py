class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = {}
        for num in nums:
            if num not in tmp:
                tmp[num] = 1
            else:
                tmp[num] += 1
        # 返回数量最大的数字1
        # cnt = 0
        # num = 0
        # for cur_num, cur in tmp.items():
        #     if cur > cnt:
        #         cnt = cur
        #         num = cur_num 
        # return num

        # 返回数量最大的数字2
        # return max(tmp, key=tmp.get)
        # 返回数量最大的数字3
        return max(tmp, key=lambda x: tmp[x])


from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Counter 返回一个特殊字典
        # most_common返回一个列表 里面是元组
        return Counter(nums).most_common(1)[0][0]