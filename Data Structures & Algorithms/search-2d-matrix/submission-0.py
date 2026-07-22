class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        t, b = 0, len(matrix) - 1
        while t <= b:
            m = (t+b)//2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                row = m
                break
            elif target > matrix[m][-1]:
                t = m + 1
            else:
                b = m - 1
        if row == -1:
            return False
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l+r)//2
            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1
        return False

        