class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # [0] - default value
        # * len(temperatures) -> length of array

        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            # calculation of value to put in array done before appending iteration to stack
            # comparing current iteration to stop of stack 
            
            while stack and t > stack[-1][0]: # [-1] -> top of stack, [0] -> index 0 - temperature
                stackT, stackInd = stack.pop() # T - temperature, Ind - index
                res[stackInd] = (i - stackInd) # difference in index

            stack.append([t, i]) # append t - temperature, i - index to the stack 

        return res # return result array
