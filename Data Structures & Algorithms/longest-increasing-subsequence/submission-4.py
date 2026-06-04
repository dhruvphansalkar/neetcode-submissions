class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # in a recursive function
        # for index i
        # iterate through i + 1 to end
        # at every index either take the value if it is greater than the current or skip
        # return max for each choice
        m = {}
        def recur(i: int) -> int:
            if i == len(nums):
                return 0
            if i in m:
                return m[i]
            maxFromHere = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    maxFromHere = max(maxFromHere, 1 + recur(j))
            m[i] = maxFromHere
            return m[i]
        for i in range(len(nums)):
            recur(i)
        return max(m.values())
            
                    
        