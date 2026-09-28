class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        res = [1] * len(nums) # Initialize new result array with 1 - default Pre

        Prefix = 1 # Initialize prefix variable to 1
        for i in range (len(nums)):
            res[i] = Prefix # Set current index of array as prefix value
            Prefix *= nums[i] # Update prefix value by multiplying with current index value
        
        postfix = 1 # initialize postfix variable to 1
        for i in range(len(nums)-1, -1, -1): # iterate from the end of the array to the beginning
            res[i] *= postfix # multiply current index value with postfix value
            postfix *= nums[i] # update postfix value by multiplying with current index value
        return res # return the result array
