class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        def backTrack(i, total, curr):
            if total == target:
                sol.append(curr[:])
                return
            if i==len(nums) or total > target:
                return
            curr.append(nums[i])
            total += nums[i]
            backTrack(i, total, curr)
            curr.pop()
            total -= nums[i]
            backTrack(i+1, total, curr)
        backTrack(0, 0, [])
        return sol

        