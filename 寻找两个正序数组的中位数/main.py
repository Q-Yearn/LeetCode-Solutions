# 前一版改进  但是时间复杂度仍是 O(m+n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        flag = 1 if total % 2 == 1 else 0
        index = (total) // 2
        i = 0
        j = 0
        tmp = []
        while len(tmp) < index + 1:
            if i >= len1:
                tmp.append(nums2[j])
                j += 1
            elif j >= len2:
                tmp.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1

        if flag:
            return tmp[-1]
        else:
            return (tmp[-1] + tmp[-2]) / 2.0  


# 还需要再理解一下        
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def getKth(index1, index2, k):
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                
                newindex1 = min(index1+ k // 2 - 1, m - 1)
                newindex2 = min(index2+ k // 2 - 1, n - 1)
                if nums1[newindex1] < nums2[newindex2]:
                    k -= newindex1 - index1 + 1
                    index1 = newindex1 + 1
                else:
                    k -= newindex2 - index2 + 1
                    index2 = newindex2 + 1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        if total % 2 == 1:
            return getKth(0, 0, total // 2 + 1)
        else:
            return (getKth(0, 0, total // 2) + getKth(0, 0, total // 2 + 1)) / 2.0


# 数学推导
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infinty = 2**40
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            num1 = -infinty if i == 0 else nums1[i-1]
            num2 = infinty if i == m else nums1[i]
            num3 = -infinty if j == 0 else nums2[j-1]
            num4 = infinty if j == n else nums2[j]

            if num1 <= num4:
                median1, median2 = max(num1, num3), min(num2, num4)
                left = i + 1
            else:
                right = i - 1
        return (median1 + median2) / 2.0 if (m + n) % 2 == 0 else median1
        