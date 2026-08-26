class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        st = []
        for i, temp in enumerate(temperatures):
            while st and st[-1][1] < temp:
                index, _ = st.pop()
                sol[index] = i - index
            st.append((i, temp))
        return sol

        