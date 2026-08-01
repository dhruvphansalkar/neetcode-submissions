class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = {}
        for task in tasks:
            m[task] = m.get(task, 0) + 1
        task_counts = [(-value, key) for key, value in m.items()]
        heapq.heapify(task_counts)
        sol = 0
        cooldown_map = {}
        while task_counts or cooldown_map:
            if (task_counts):
                count, task = heapq.heappop(task_counts)
                if count + 1 != 0:
                    cooldown_map[task] = (count + 1, n)
            sol += 1
            key_to_delete = ''
            for key, (count, cooldown) in cooldown_map.items():
                cooldown_map[key] = (count, cooldown - 1)
                if cooldown == 0:
                    heapq.heappush(task_counts, (count, key))
                    key_to_delete = key
            if key_to_delete != '':
                del cooldown_map[key_to_delete]
        return sol

        