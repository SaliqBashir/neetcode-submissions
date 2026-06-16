class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowHigh = len(matrix) - 1
        columnHigh = len(matrix[0]) - 1
        rowLow = 0
        columnLow = 0
        while rowLow <= rowHigh:
            row = (rowLow + rowHigh) // 2
            if target > matrix[row][-1]:
                rowLow = row + 1
            elif target < matrix[row][0]:
                rowHigh = row - 1
            else:
                break

        if not (rowLow <= rowHigh):
            return False

        row = (rowLow + rowHigh) // 2
        while columnLow <= columnHigh:
            columnMid = (columnLow + columnHigh) // 2

            if target == matrix[row][columnMid]:
                return True
            elif target < matrix[row][columnMid]:
                columnHigh = columnMid - 1
            else:
                columnLow = columnMid + 1
        return False

        