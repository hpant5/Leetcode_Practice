#this was an interesting problem leetcode puts this in medium category but its just tricky
#the solution i have come up with may not be the most optimized one but it works 
#probelm:

#You are given an integer array heights where heights[i] represents the height of the tower find maximum container volume

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        temp = 0
        for i,j in enumerate(heights):
            for m,n in enumerate(heights):
                if i!=m:
                    a = min(j,n)
                    b = abs(i-m)
                    max_n = a*b
                    if max_n>temp:
                        temp = max_n
                    else:
                        continue
                else:
                    continue
        return temp
        

