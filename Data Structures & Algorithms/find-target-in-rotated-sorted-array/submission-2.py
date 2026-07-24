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

        def binarySearch(l: int, r: int) -> int:
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m -1
            return -1
        if pivot == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[pivot - 1]:
            l, r = 0, pivot - 1
        else:
            l, r = pivot, len(nums) - 1
        return binarySearch(l, r)
        