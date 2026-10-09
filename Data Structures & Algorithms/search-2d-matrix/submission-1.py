class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        col = len(matrix[0])

        top, bottom = 0, rows - 1
        row = -1

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target:
                row = mid
                top = mid + 1
            else:
                bottom = mid - 1

        if row == -1:
            return False

        if target > matrix[row][col - 1]:
            return False

        left, right = 0, col - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
