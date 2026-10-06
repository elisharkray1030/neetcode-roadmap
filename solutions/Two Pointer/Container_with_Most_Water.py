class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 # initializing result
        l, r = 0, len(heights) - 1 # initializing left and right pointers

        while l < r:
            area = (r - l) * min(heights[l], heights[r]) # Area calculation
            # r - l - using indices to calculate base/ width
            # min(heights[l], heights[r]) - using the minimum height to calculate the height of the container

            res = max(res, area) # max() to update res if area is greater than res

            # cases to move the pointers
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res