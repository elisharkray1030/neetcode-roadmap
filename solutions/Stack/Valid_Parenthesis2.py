class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:                          # odd length is always invalid
            return False
        stack = []
        for c in reversed(s):                   # scan right → left
            if c in "([{":                      # opener: behaves like a closer here
                if not stack or ord(stack[-1]) - ord(c) not in (1, 2):
                    return False                # also catches opener with no closer to its right
                stack.pop()
            else:
                stack.append(c)                 # closer: behaves like an opener here
        return not stack