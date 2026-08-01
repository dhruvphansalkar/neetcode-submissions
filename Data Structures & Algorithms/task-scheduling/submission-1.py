class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            if q and q[0][1] <= time:
                count, _ = q.popleft()
                heapq.heappush(heap, count)
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count != 0:
                    q.append((count, time + n + 1))
            time += 1
        return time