class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        index = (len1 + len2) // 2
        flag = 0
        if (len1 + len2) % 2 != 0:
            flag = 1
        else:
            flag = 0
        i = 0
        j = 0
        tmp = []
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
            if len(tmp) - 1 == index:
                if flag:
                    return tmp[-1]
                else:
                    return (tmp[-1] + tmp[-2]) / 2.0

        while i < len1:
            tmp.append(nums1[i])
            i += 1
            if len(tmp) - 1 == index:
                if flag:
                    return tmp[-1]
                else:
                    return (tmp[-1] + tmp[-2]) / 2.0  

        while j < len2:
            tmp.append(nums2[j])
            j += 1
            if len(tmp) - 1 == index:
                if flag:
                    return tmp[-1]
                else:
                    return (tmp[-1] + tmp[-2]) / 2.0  
