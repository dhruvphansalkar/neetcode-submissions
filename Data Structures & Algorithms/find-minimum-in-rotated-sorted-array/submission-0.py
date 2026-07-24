class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if number at right is less than number at left, that means solution in between them
        # if left < right that means solution is left

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
        