# 完全平衡二叉树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST_range(nums: List[int], begin: int, end: int) -> Optional[TreeNode]:
        if begin > end:
            return None
        l = end - begin + 1
        # 算出高度
        d = l.bit_length()
        if d == 1:
            leftNodes = 0
        else:
            # 第一项是填满最后一层左边的情况 第二项可能填不满左边或者超出左边
            leftNodes = min((1 << (d - 1)) - 1, l - (1 << (d - 2)))
        root_idx = begin + leftNodes
        root = TreeNode(nums[root_idx])
        root.left = sortedArrayToBST_range(nums, begin, root_idx - 1)
        root.right = sortedArrayToBST_range(nums, root_idx + 1, end)
        return root

    # 方便调用的 wrapper
    def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
        return sortedArrayToBST_range(nums, 0, len(nums) - 1)