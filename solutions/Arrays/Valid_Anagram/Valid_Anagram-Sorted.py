# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.

# Sorting method depends on how efficient the sorting algorithm is. 
# Python uses Timsort which has a time complexity of O(n log n). 
# The space complexity is O(1) if we sort in place, or O(n) if we create a new sorted list.

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t) # Sort both strings and compare them