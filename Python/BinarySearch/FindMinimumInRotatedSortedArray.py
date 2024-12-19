class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        curr_min = float("inf")


        while left < right:
            mid = (left + right) // 2
            curr_min = min(curr_min, nums[mid])


            if nums[mid] > nums[right]:
                left = mid+1
            
            else:
                 right = mid - 1

        return min(curr_min, nums[left])


