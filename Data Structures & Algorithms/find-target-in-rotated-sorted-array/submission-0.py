class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r)//2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        pivot = l

        l, r = 0, pivot - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m -1
        
        l, r = pivot, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m -1
        return -1
        