class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #since everything is in sorted order, you can check the first element
        #in each row, and do a binary search
        #after, find the row that the number is in -> then do another binary search on that row
        #then return true if the number exists in the matrix
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom: 
            mid = (top + bottom) // 2
            if target < matrix[mid][0]: 
                bottom = mid - 1
            elif target > matrix[mid][0]: 
                top = mid + 1
            else: 
                return True 
                
        row = bottom 
        left = 0
        right = len(matrix[row]) - 1

        while left <= right: 
            mid = (left + right) // 2
            if target == matrix[row][mid]: 
                return True
            elif target < matrix[row][mid]: 
                right = mid - 1
            else: 
                left = mid + 1
            
        return False