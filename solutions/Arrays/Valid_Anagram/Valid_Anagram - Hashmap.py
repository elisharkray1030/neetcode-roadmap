# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t): # If the lengths are different, they cannot be anagrams
            return False

        countS, countT = {}, {} # Create two dictionaries (Key - character, Value - count)

        for i in range(len(s)): # Building Hashmaps for both strings
            countS[s[i]] = 1 + countS.get(s[i], 0) # Count the characters in s
            countT[t[i]] = 1 + countT.get(t[i], 0) # Count the characters in t
            # index in created dictionary
            # .get -> If the key exists, return its value. If not, return the default value (0 in this case)

        for c in countS: # Compare the two dictionaries
            if countS[c] != countT.get(c, 0): # If the counts are different, return False
                return False
        return True # If all counts are the same, return True

        
