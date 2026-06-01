class Solution:
    from collections import deque
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize = 0
        window = deque()
        count = defaultdict(int)
        for char in s:
            count[char] += 1
            window.append(char)
            while count[char] > 1:
                removed = window.popleft()
                count[removed] -= 1
            maxSize = max(len(window), maxSize)
        return maxSize