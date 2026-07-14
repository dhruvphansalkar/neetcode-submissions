class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def backTrack(i, curr):
            if i == len(nums):
                sol.append(curr[:])
                return
            curr.append(nums[i])
            backTrack(i+1, curr)
            curr.pop()
            backTrack(i+1, curr)
        backTrack(0, [])
        return sol

