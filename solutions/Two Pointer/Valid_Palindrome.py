class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # initialize pointers
        # l = 0 - start
        # r = len(s) - 1 - end of string

        while  l < r: # whilst left is still on the left of right

            while l < r and not self.isAlphanum(s[l]): # calling func to determine if alpha num, if not -> continue by iterating
                l += 1
            while r > l and not self.isAlphanum(s[r]): # same as above
                r -= 1
            if s[l].lower != s[r].lower(): # comparing values when converted to lower
                return False
            l, r, = l + 1, r - 1 # iterate 
        return True # finished while loop -> Palindrome

    def isAlphanum(self, c): # Alphanum - a - z/ A - Z/ 0 - 9
        # use ASCII to determine True or False
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))
