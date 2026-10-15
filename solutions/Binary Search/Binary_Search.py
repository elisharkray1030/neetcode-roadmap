class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # initializing 2 pointers

        while l <= r: # 2 pointer method
            m = (l + r) // 2 # calculating mid point

            # modifying r and l depending on condition
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1
