class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # initialize stack

        for c in tokens: # iterate through array
        # if and elif conditions for 4 operators
        # else condition for integers
        # int() for appending integers

            if c == "+":
                stack.append(stack.pop() + stack.pop()) # pop twice -> add up -> append (push)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a) # make sure b - a
            elif c == "*":
                stack.append(stack.pop() * stack.pop()) # pop twice -> multiply -> append
            elif c == "/":    
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a)) # for / operator need to specify b/a
            else:
                stack.append(int(c))

        return stack[0] # returning final value - only value left on stack -> [0]

# Time and Space - O(n)