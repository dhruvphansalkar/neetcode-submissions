class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_list = [((x**2 + y**2)**(1/2), x, y) for x, y in points]
        heapq.heapify(distance_list)
        sol = []
        i = 0
        while i < k:
            _, x, y = heapq.heappop(distance_list)
            sol.append([x, y])
            i += 1
        return sol
        