class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        rear = len(heights) - 1
        maxSpace = 0
        while front <= rear:
            space = min(heights[front], heights[rear]) * (rear - front)
            if space > maxSpace:
                maxSpace = space
            if heights[front] > heights[rear]:
                rear -= 1
            else:
                front += 1
        return maxSpace