class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ''
        lst = self.m[key]
        if len(lst) == 0 or timestamp < lst[0][0]:
            return ''
        l, r = 0, len(lst) - 1
        sol = ''
        while l <= r:
            m = (l + r) // 2
            if timestamp >= lst[m][0]:
                sol = lst[m][1]
                l = m + 1
            else:
                r = m - 1
        return sol
