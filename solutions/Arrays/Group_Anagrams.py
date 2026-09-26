# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        res = {} # mapping charCount to list of Anagrams

        for s in strs: # loop through the array strs
            key = tuple(sorted(s)) # tuple - ('', '', '') | list - ['', '', '']
            # "eat" → ['a', 'e', 't'] → ('a', 'e', 't')
            # "tea" → ['a', 'e', 't'] → ('a', 'e', 't')
            # "tan" → ['a', 'n', 't'] → ('a', 'n', 't')
            # key = characters in order
            if key not in res: # key not found in {}
                res[key] = []  # create new list?
            res[key].append(s) # append on existing sublist (key)
        return list(res.values()) # return only values of res in form of list



# Time: O(n * k log k) - sort each of n words, each up to k characters long.
# Space: O(n * k) - store the words and their sorted-letter keys.
