class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = [] # result array 
        nums.sort() # sorting the array to use two pointer technique
        
        for i, a in enumerate(nums): # enumerate -> return index and value of the array
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1 # two pointer technique

            while l < r:
                three_sum = a + nums[l] + nums[r] # calculate the sum of the three numbers

                if three_sum > 0: # if the sum is greater than 0, move the right pointer to the left
                    r -= 1
                elif three_sum < 0: # if the sum is less than 0, move the left pointer to the right
                    l += 1
                else: # if the sum is equal to 0, add the triplet to the result array
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # skip duplicates for the left pointer
                        l += 1
        return res # array of buckets of triplets that sum to 0