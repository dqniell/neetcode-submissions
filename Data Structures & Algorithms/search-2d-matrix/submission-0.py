class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom: 
            mid = top + (bottom - top) // 2

            if target < matrix[mid][0]: 
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else: 
                break

        row = mid
        left = 0
        right = len(matrix[0]) - 1

        while left <= right: 
            mid = left + (right - left) // 2

            if target == matrix[row][mid]: 
                return True
            elif matrix[row][mid] < target: 
                left = mid + 1
            else: 
                right = mid - 1
        
        return False