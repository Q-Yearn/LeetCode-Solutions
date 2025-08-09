class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])
        length = len(intervals)
        for i in range(1, length):
            # flag = 0
            # 排序之后就不需要遍历整个result来看是否有重合了
            # for j in range(len(result)):
            #     if result[j][0] <= intervals[i][0] <= result[j][1]:
            #         flag = 1
            #         if intervals[i][1] > result[j][1]:
            #             result[j][1] = intervals[i][1]
            #         break         
            # if flag == 0:
            #     result.append(intervals[i])

            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result
