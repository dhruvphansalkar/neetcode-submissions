class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(l, r, needle):
            while l <= r:
                m = (l + r) // 2
                if numbers[m] == needle:
                    return m
                if needle > numbers[m]:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        for i, num in enumerate(numbers):
            index = binarySearch(i + 1, len(numbers) - 1, target - num)
            if index != -1:
                return [i + 1, index + 1]
        return [0, 0]
        