# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lis2 = sorted(set(nums))
        if len(lis2) ==0:
            return 0
        counter =1 
        max_num =1 
        for i in range(1,len(lis2)):
            if (lis2[i-1]+1) == (lis2[i]):
                counter += 1
                if counter > max_num:
                    max_num = counter 
            else: 
                counter = 1
        return max_num