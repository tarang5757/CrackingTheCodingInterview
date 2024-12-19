

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left pointer and right pointer
        l = 0
        r = len(nums)-1
        
        while l <= r:
            #middle index
            mid = (l + r) // 2

            #if the value at middle index == target value
            if nums[mid] == target:
                #return the index of the middle value
                return mid
            
            elif target > nums[mid]:
                l = mid + 1

            elif target < nums[mid]:
                r = mid - 1

        return -1

            
    
        


