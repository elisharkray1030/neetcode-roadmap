class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        stack = []


        for p, s in sorted(pair)[::-1]: # Reversed Sorted Order

            stack.append((target - p) / s) # append time to stack

            # if time if prior is less than later -> collision
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # collide condition and stack has more than 1 element
                stack.pop() # pop if collide to 1 stack 
                # removing the one initially further from target
        
        return len(stack) # no. of fleets


# Time - O(nlogn)
# sorted -> log n
# Space - O(n)