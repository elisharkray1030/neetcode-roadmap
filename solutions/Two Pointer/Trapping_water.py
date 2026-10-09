class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r, = 0, len(height) - 1 # poiter initialization
        leftMax, rightMax = height[l], height[r] # variable initialization
        res = 0 # initializing result

        while l < r: # two pointer technique

            if leftMax < rightMax: # iteration 
                l += 1

                leftMax = max(leftMax, height[l]) # updating left max

                res += leftMax - height[l] # appending to result

            else:  # iteration 
                r -= 1
                rightMax = max(rightMax, height[r]) # updating right max
                
                res += rightMax - height[r] # appending to result

        return res  
        