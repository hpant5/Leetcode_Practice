#problem :Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for i in range(0,len(nums)):
            for j in nums:
                sumt = nums[i]+j
                if sumt==target and i != nums.index(j):
                    final.append(i)
                    final.append(nums.index(j))
                    return sorted(final)
