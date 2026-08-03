class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        pq = []
        for key, val in count.items():
            pq.append((-val, key))
        heapq.heapify(pq)
        sol = []
        while pq and k > 0:
            _, key = heapq.heappop(pq)
            sol.append(key)
            k -= 1
        return sol
