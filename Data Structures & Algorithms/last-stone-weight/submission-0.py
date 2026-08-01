class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while stones:
            largest = heapq.heappop(stones)
            if stones:
                second_largest = heapq.heappop(stones)
                if second_largest == largest:
                    continue
                else:
                    heapq.heappush(stones, largest - second_largest)
            else:
                return -largest
        return 0
            
            
            
        