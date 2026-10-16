class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:        
            m = (l + r) // 2 # get mid point

            # return target
            if nums[m] == target:
                return m

            # left portion
            # if target is right portion - search right
            if nums[l] <= nums[m]:
                # go right if target larger than m
                # go right if target smaller than min in range
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                # move m to left if target smaller than m
                else:
                    r = m - 1

            # right portion
            else:
                # go left if target smaller
                # go left or go to left portion if target larger than range
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                # move m to the right if target larger than m
                else:
                    l = m + 1

        # not found
        return -1

# checking max and min in range with l, r
    # right portion - need check if target larger than range
        # compare with r in right portion
        # if target > than nums[r] -> left 
    # left portion - need check if target smaller than range
        # compare with l in left portion
        # if target < than nums[l] -> right 
# comparing m with target
    # if target smaller -> left - r = m - 1
    # if target larger -> right - l = m + 1