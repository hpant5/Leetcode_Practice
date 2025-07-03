# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums)==1:
            return 1
        elif len(nums)==0:
            return 0
        max1,counter = 1,1
        for j in range(1,len(nums)):
            if nums[j-1]+1 == nums[j]:
                counter = counter +1
                max1 = max(max1,counter)
            else:
                counter = 1
        return max1