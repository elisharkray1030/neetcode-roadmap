class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # set 
        res = 0

        for n in nums:
            # guard: only start at the beginning of a run
            if (n - 1) not in numSet:
                cur = n          # pointer to the current number we're checking
                counter = 0      # length of the run found so far
                while cur in numSet:
                    counter += 1
                    cur += 1     # walk forward one step
                res = max(counter, res)

        return res
    
# if statement - check if we are start of sequence 
    # -> reset curr pointer, reset counter = 0
# while -> update pointer and counter -> if in set -> max function