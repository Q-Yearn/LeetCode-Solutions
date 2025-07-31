# 因为可能出现 开始前两个不能合并  但是和后面的合并之后  合共区间可以和之前合并了  所以错了 需要先排序
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
        flag = 0
        for j in range(len(result)):
            if result[j][0] <= intervals[i][0] <= result[j][1]:
                flag = 1
                if intervals[i][1] > result[j][1]:
                    result[j][1] = intervals[i][1]
                break
            # 排序之后就不会出现这种情况了
            # elif intervals[i][0] <= result[j][0] <= intervals[i][1]:
            #     flag = 1
            #     if  result[j][1] < intervals[i][1]:
            #         result[j][0] = intervals[i][0]
            #         result[j][1] = intervals[i][1]
            #     else:
            #         result[j][0] = intervals[i][0]
            #     break              
        if flag == 0:
            result.append(intervals[i])
     return result
