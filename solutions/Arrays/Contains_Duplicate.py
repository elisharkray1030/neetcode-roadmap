class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # set in python

        for n in nums:
            if n in hashset: # if in set -> return true
                return True
            hashset.add(n)   # not in set -> add to set -> continue for loop
        return False