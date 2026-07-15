class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        def recur(i, curr):
            if i == len(nums):
                sol.append(curr[:])
                return
            curr.append(nums[i])
            recur(i+1, curr)
            curr.pop()
            currentVal = nums[i]
            while i < len(nums) and nums[i] == currentVal:
                i+=1
            recur(i, curr)
        recur(0, [])
        return sol
        