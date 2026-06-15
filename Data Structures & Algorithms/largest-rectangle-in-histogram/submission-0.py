class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        rectangle = 0
        heights.append(0)
        for index, height in enumerate(heights):
            while stack and stack[-1][1] > height:
                _, popped_height = stack.pop()
                if stack:
                    width = index - stack[-1][0] - 1
                else:
                    width = index
                rectangle = max(rectangle,popped_height * width)
            stack.append([index, height])
        return rectangle