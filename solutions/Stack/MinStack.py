class MinStack:

    def __init__(self): # initializing the 2 arrays - stacks
        self.stack = [] # self. because it is inside a class
        self.minStack = []


    def push(self, val: int) -> None: # push function
        self.stack.append(val) # val ac
        # check if minStack is empty
        if self.minStack:
            val = min(val, self.minStack[-1]) # comparing current val with last known mincepted by function appended to stack

            # -1 - LIFO
        else:
            val = val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() # update the min
        

    def top(self) -> int:
        return self.stack[-1] # -1 - LIFO
        

    def getMin(self) -> int:

        if self.minStack:
            return self.minStack[-1] # -1 - LIFO
        else:
            return 
        
