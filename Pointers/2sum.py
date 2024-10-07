class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li = []
        for i,j in enumerate(numbers):
            for m,n in enumerate(numbers):
                if m !=i:
                    if j+n == target:
                        li.append(i+1)
                        li.append(m+1)
                        return li
                else:
                    continue
#problem statement : find the two indices ( distinct) which when added make up the target. 