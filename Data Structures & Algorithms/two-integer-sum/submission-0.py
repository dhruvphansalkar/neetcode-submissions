class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            if target - num in m:
                return [m[target - num], i]
            m[num] = i
        return -1
        