class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        seen = set()

        def recur(curr):
            if len(curr) == len(nums):
                sol.append(curr[:])
                return
            for index, num in enumerate(nums):
                if index in seen:
                    continue
                curr.append(num)
                seen.add(index)
                recur(curr)
                curr.pop()
                seen.remove(index)
        recur([])
        return sol
                

        