class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)
            self.rebalance()
            print(self.small)
            print(self.large)
            print(num)
            return

        heapq.heappush(self.small, -num)
        self.rebalance()
        print(self.small)
        print(self.large)
        print(num)

        

    def rebalance(self):
        if len(self.large) - len(self.small) == 2:
            element = heapq.heappop(self.large)
            heapq.heappush(self.small, -element)
        if len(self.large) - len(self.small) == -2:
            element = heapq.heappop(self.small)
            heapq.heappush(self.large, -element)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        small_val = self.small[0] if len(self.small) > 0 else 0
        large_val = self.large[0] if len(self.large) > 0 else 0
        return (-small_val + large_val) / 2
        
        