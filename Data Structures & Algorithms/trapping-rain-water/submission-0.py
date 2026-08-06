class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max, r_max = [0] * n, [0] * n
        for i in range(n):
            l_max[i] = max(l_max[i-1] if i - 1 >= 0 else 0, height[i])
            r_max[n - i - 1] = max(r_max[n - i] if n - i < n else 0, height[n - i - 1])
        sol = 0
        for i, h in enumerate(height):
            sol += min(l_max[i], r_max[i]) - h
        return sol


                

        