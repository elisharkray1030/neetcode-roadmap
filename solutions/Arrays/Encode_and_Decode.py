class Solution:

    def encode(self, strs: List[str]) -> str: 
        res = "" # Initialize string - encoded form 

        for s in strs: # loop through array of strings 
            res += str(len(s)) + "#" + s # length of string (integer) + # + string (s)
        return res # return

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # initialize array and pointer

        while i < len(str): # while pointer is less than the length of the string 
            j = i # set another pointer == i
            while str[j] != "#": # looping through initial part (integers) -> attain length of string
                j += 1 # iterate ...

            length = int(str[i:j]) # len(s) == integer from i:j - slicing

            res.append(str[j + 1 : j + 1 + length]) # append j + 1 -> j + 1 + length 
            # str[j] -> "#" - which is why j + 1
            # j + 1 (start of string)
            # j + 1 + length (last char)

            i = j + 1 + length 
            # iterate pointer i to next string - should be integer or i > / == len(str) -> break
            
        return res
