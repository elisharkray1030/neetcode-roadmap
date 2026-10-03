class Solution:
    def twoSum(self,numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 # initialize pointers

        # while left is still left of r
        while l < r:
            curSum = numbers[l] + numbers[r] # sum of current state of pointer

            # compare to target
            if curSum > target: # larger than target r - 1
                r -= 1
            elif curSum < target: # smaller than target l + 1
                l += 1
            else:
                return [l + 1, r + 1] # return indices 

        return [] # fallback return if no solution