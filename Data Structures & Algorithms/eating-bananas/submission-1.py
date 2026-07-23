class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1
        def hoursToEatAllBananas(speed):
            total = 0
            for pile in piles:
                total += math.ceil(pile/speed)
            return total
        
        l, r = 1, max(piles)
        sol = r
        while l < r:
            m = (l + r)//2
            if hoursToEatAllBananas(m) <= h:
                r = m
            else:
                l = m + 1
        return l


        