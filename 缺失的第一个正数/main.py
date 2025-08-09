class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while(nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]):
                # 不能这么写  因为nums[i]会先被修改  然后进而影响nums[nums[i] - 1]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1