class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        sol = -1
        for i in range(k):
            sol = heapq.heappop(nums)
        return -sol
        