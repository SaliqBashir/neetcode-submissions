class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowHigh = len(matrix) - 1
        columnHigh = len(matrix[0]) - 1
        rowLow = 0
        columnLow = 0
        while rowLow <= rowHigh:
            rowMid = rowLow + (rowHigh - rowLow) // 2
            columnMid = columnLow + (columnHigh - columnLow) // 2

            if target == matrix[rowMid][columnMid]:
                return True

            elif target > matrix[rowMid][columnMid]:
                low = columnMid
                high = columnHigh
                while low <= high:
                    mid = low + (high - low) // 2
                    if target == matrix[rowMid][mid]:
                        return True
                    if target > matrix[rowMid][mid]:
                        low = mid + 1
                    if target < matrix[rowMid][mid]:
                        high = mid - 1
                rowLow = rowMid + 1

            else:
                low = columnLow
                high = columnMid
                while low <= high:
                    mid = low + (high - low) // 2
                    if target == matrix[rowMid][mid]:
                        return True
                    if target > matrix[rowMid][mid]:
                        low = mid + 1
                    if target < matrix[rowMid][mid]:
                        high = mid - 1
                rowHigh = rowMid - 1
        return False
