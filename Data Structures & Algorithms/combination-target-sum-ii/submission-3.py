class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates.sort()
        def recur(i, total, curr):
            if total == target:
                sol.append(curr[:])
                return
            if i == len(candidates) or total >= target:
                return
            curr.append(candidates[i])
            total += candidates[i]
            recur(i+1, total, curr)
            curr.pop()
            total -= candidates[i]
            currentVal = candidates[i]
            while i < len(candidates) and candidates[i] == currentVal:
                i+=1
            recur(i, total, curr)
        recur(0, 0, [])
        return sol
        