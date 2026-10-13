class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h: # stack not empty and top of stack larger than height
                index, height = stack.pop() # popping index and height

                # updating max
                maxArea = max(maxArea, height * (i - index)) # calculation of area height * width
                # width = height * start index - index of top of stack -- difference

                start = index # iteration, moving the start index 
                # how far at this height can a rectangle extend to the left

            stack.append((start, h))  # updating the top of stack with
            # start - index of bar
            # h - height of bar

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) # calculation of area of how far the rectangle extends
        return maxArea