class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(len(height)):
            maxLeft = 0
            maxRight = 0
            for j in range(0, i, 1):
                if height[j] > maxLeft:
                    maxLeft = height[j]
            for k in range(len(height)-1, i, -1):
                if height[k] > maxRight:
                    maxRight = height[k]
            sum = min(maxLeft, maxRight) - height[i]
            if sum > 0:
                water += sum
        return water