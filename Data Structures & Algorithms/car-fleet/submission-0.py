class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_sorted_by_position = []
        for i in range(len(position)):
            time_sorted_by_position.append((position[i], (target - position[i])/speed[i]))
        time_sorted_by_position.sort(key = lambda x: -x[0])

        fleet = []
        sol = 0
        for _, time in time_sorted_by_position:
            if not fleet or time > fleet[-1]:
                sol += 1
                fleet.append(time)
        return sol
        