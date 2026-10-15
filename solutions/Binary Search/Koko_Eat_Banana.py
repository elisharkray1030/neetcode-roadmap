class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # initializing 2 pointers
        res = r # max in the piles - definately will work

        while l <= r: # 2 pointer method
            k = (l + r) // 2 # calculating mid point
            hours = 0 # initializing hours

            for p in piles:
                hours += math.ceil(p / k) # calculating hours taken to eat all bananas at speed k
                # ceil - rounds up to the nearest integer - if p/k is not an integer, it will round up to the next integer
                # koko can only eat from 1 pile per hour, so if p/k is not an integer, it will take koko an extra hour to finish the pile

            if hours <= h: # if hours taken is less than or equal to h
                res = k # update res to k
                r = k - 1 # move right pointer to left
            else:
                l = k + 1 # move left pointer to right
        
        return res
