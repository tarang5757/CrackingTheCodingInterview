class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        total = 0
        res = float('inf')

        for  r in range(len(nums)):

            #expand the window
            total += nums[r]

            #shrink the window
            while total >= target:
                #calculate the minimum length of subarray (in this case the length of the window. we do +1 because pointers are index based )
                res = min(res, r-l+1)

                total -= nums[l]
                l+= 1

        return res if res != float("inf") else 0



        

