class solution:
    def minSubarray(self , target: int , nums:list[int])-> int:
        l , total = 0 , 0 
        res = float(-inf)
        for r in range(len(nums)):
            total = total + nums[r]
            if total >= target:
                res = min(r-1+l, res)
        return 0 if res == float("inf") else res