# Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        HashMap = {} # val : index

        for i, n in enumerate(nums): # enumerate -> i - index, n - value
            diff = target - n 
            if diff in HashMap: 
                return [HashMap[diff], i] # return the index of the diff and the current index
            HashMap[n] = i
        return 


# enumerate 
# Output: (0, 2) (1, 7) (2, 11) (3, 15) (4, 20)

# diff = target - n => diff = target value - current value

# diff found in hashmap -> return the index of the diff and the current index

# else add hashmap with the current value and its index