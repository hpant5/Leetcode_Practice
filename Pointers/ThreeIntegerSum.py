# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets


# the solution works but may be not be themsot efficient solution will work on finding the most efficient solution later 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = []
        for i,j in enumerate(nums):
            for m,n in enumerate(nums):
                for p,q in enumerate(nums):
                    if i!=m and m!=p and i!=p:
                        if j+n+q==0:
                            li= []
                            li.append(j)
                            li.append(n)
                            li.append(q)
                            li = sorted(li)
                            if li not in temp:
                                temp.append(li)
                            else:
                                continue
                    else:
                        continue
        return temp    
