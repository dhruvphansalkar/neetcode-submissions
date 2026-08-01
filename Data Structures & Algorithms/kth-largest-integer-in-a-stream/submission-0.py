class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [num for num in nums]
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)        

    def add(self, val: int) -> int:
        if len(self.nums) == self.k:
            heapq.heappushpop(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
        return self.nums[0]
        
