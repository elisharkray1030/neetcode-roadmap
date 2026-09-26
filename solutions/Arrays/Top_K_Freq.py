class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # hashmap number:frequency


        freq = [[] for i in range(len(nums) + 1)]
        # [[]] - sublist, or buckets
        # for loop on the same line - number of these sublsts, buckets
        # len(nums) - maximum amt of times possible + 1

        for n in nums: # loop through array of integers (nums)
            count[n] = 1 + count.get(n,0) 
            # count[n] - indices dict by n - key
            # count.get(n,0) - look up key n, not there then set 0, .get does not insert, only searches up
            # 1 + add 1 to value
        for n, c in count.items(): # .items -> return both (key, value)
        # n - number
        # c - frequency
            freq[c].append(n)
            # index by c
            # append number - n into bucket
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # reading array in reverse 
        # start - len(freq) - 1
        # end - 0
        # increment - -1
            for n in freq[i]: # loop each bucket
                res.append(n) # append values in bucket to res
                if len(res) == k: # res == k -> top k values have been appended
                    return res

