class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1


        
        while l <= r:

            # works for n = n
            # after bottom else condition -> get to right portion
            # if l < r -> successfully ignored portion
            # get min of recorded res and [l]
            if nums [l] < nums[r]: 
                res = min(res, nums[l]) # safe as well for n = n as res is updated at the start, most left element would be min 
                break
        
            m = (l + r) // 2 # get mid point
            res = min(res, nums[m]) # update res min

            
            if nums[m] >= nums[l]: # condition to determine if we are in the correct portion or not 
                l = m + 1
            else:
                r = m - 1
            
        return res

