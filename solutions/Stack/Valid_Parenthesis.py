class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:                          # odd length is always invalid
            return False
        stack = [] # initialize stack
        closeToOpen = {")" : "(", # initialize hashmap for cross reference
                        "}" : "{",
                        "]" : "["}

        for c in s: # for loop to loop through string s

            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # matching then we continue -> pop
                    stack.pop()
                else:
                    return False # not match -> false
            else:
                stack.append(c) # append to stack if not found
                

        return True if not stack else False # return True if stack empty


            