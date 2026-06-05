class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxWindow = []
        l = 0
        r = k - 1
        window = deque()
        for i in range(k):
            window.append(nums[i])

        for i in range(k,len(nums)):
            maxWindow.append(max(window))
            window.append(nums[i])
            window.popleft()
        maxWindow.append(max(window))
        return maxWindow