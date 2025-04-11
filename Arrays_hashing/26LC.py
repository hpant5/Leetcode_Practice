class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        l = 1  # points to where the next unique value should go
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:  # found a new unique element
                nums[l] = nums[r]
                l += 1
        return l 