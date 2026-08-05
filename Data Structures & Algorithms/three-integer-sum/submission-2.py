class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(l, r, target):
            combos = []
            seen = set()
            while l < r:
                if nums[l] + nums[r] == target:
                    combos.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            return combos
        sol = []
        i = 0
        while i < len(nums):
            num = nums[i]
            combos = twoSum(i + 1, len(nums)-1, -num)
            for num2, num3 in combos:
                sol.append([num, num2, num3])
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            i = j
        return sol
        