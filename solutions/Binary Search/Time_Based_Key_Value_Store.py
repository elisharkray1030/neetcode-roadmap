class TimeMap:

    def __init__(self):
        self.store = {} # key = string : value = [list of [value, time]]

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: # add to the hashmap if string is not found
            self.store[key] = []

        self.store[key].append([value, timestamp]) # add the value and time

    def get(self, key: str, timestamp: int) -> str:
        res = "" # initialize res
        values = self.store.get(key, []) # set values

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # valid value
                res = values[m][0] # set res - closest valid value 
                # sometimes not exact timestamp but can be smaller than timestamp same value
                l = m + 1 # update pointer

            else: # invalid value if larger
                r = m - 1 # update pointer
        
        
        return res

        
